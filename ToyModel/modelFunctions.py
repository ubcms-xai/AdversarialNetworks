# modelFunctions.py


import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import math
import time
import h5py
import sklearn
import copy
from sklearn.utils import shuffle
from scipy import stats
import os

# getXY
# getDataset
# calc_loss_total
# train_step

def getXY(trainfile, testfile, features, split, N):
    
    # returns train and test dictionaries from files
    # split: train dataset fraction
    
    if(split > 0.999):
        print('splitting 95% training, 5% validation')
        split = 0.95
    
    nsplit = int(N*split)
    
    
    X_trn = {key: trainfile[key][:nsplit] for key in features}
    Y_trn = trainfile['labels'][:nsplit]
    X_tst = {key: testfile[key] for key in features}
    Y_tst = testfile['labels']
    X_val = {key: trainfile[key][nsplit:] for key in features}
    Y_val = trainfile['labels'][nsplit:]
    
    X_trn['theta'] = X_trn['theta'][:,0]
    X_tst['theta'] = X_tst['theta'][:,0]
    X_val['theta'] = X_val['theta'][:,0]
    
    # reshape for additional dimension of 1
    for key in features:
        
        shape_trn = X_trn[key].shape
        shape_tst = X_tst[key].shape
        shape_val = X_val[key].shape
        
        if( shape_trn[-1] > 1):
            X_trn[key] = X_trn[key].reshape(*shape_trn, 1)
        if( shape_tst[-1] > 1):
            X_tst[key] = X_tst[key].reshape(*shape_tst, 1)
        if( shape_val[-1] > 1):
            X_val[key] = X_val[key].reshape(*shape_val, 1)
            
            
    
    
    return X_trn, Y_trn, X_tst, Y_tst, X_val, Y_val


def getDataset(X, Y, batchSize):
    
    # returns batched tf.data.Dataset from dictionary
    
    dataset = tf.data.Dataset.from_tensor_slices((X, Y))
    dataset = dataset.batch(batchSize)
    
    return dataset
 
def calc_loss_total(loss_c, loss_a, Lambda):

    # loss_c  - loss of classifier
    # loss_a  - loss of adversary
    
    loss_c = tf.cast(loss_c, 'float32')
    loss_a = tf.cast(loss_a, 'float32')

    L = tf.math.abs(tf.reduce_mean(loss_c - Lambda * loss_a))
    
    return L, Lambda



@tf.function
def train_step(X_c, Y_c, X_a, Y_a, classifier, adversary, model, Lfn_a, Lfn_c, optimizer, Lambda):
    
    # X_c : classifier dataset for batch
    # Y_c : classifier labels for batch
    # X_a : adversary dataset for batch
    # Y_a : adversary labels for batch
    # Lfn_c : classifier loss function
    # Lfn_a : adversary loss function
    
    
    with tf.GradientTape(persistent=True) as tape_class:

        # adversary output and labels for the batch
        logits_adv = adversary([classifier(X_c), X_a])

        # classifier output for the batch
        logits_class = classifier(X_c) 

        # get classifier loss
        loss_class = Lfn_c(logits_class, Y_c)

        # get adversary loss
        loss_adv = Lfn_a(logits_adv, Y_a)
        
        # get combined loss
        loss_total = calc_loss_total(loss_class, loss_adv, Lambda)

        tape_class.watch(loss_class)
        tape_class.watch(loss_total)
        tape_class.watch(model.trainable_weights)

    # get gradients
    grads = tape_class.gradient(loss_total, model.trainable_weights)            

    # apply gradients
    optimizer.apply_gradients(zip(grads, model.trainable_weights))
    
    return loss_total, loss_class, loss_adv




