# functions.py


import pandas as pd


import tensorflow as tf

# Helper libraries
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

# printTime
# plotFeature
# getAdversary
# plotBin
# get_prediction_yvalues



xlabels = {
'theta':r'$\Delta \theta$',
'z':r'$\mathrm{log}(z)$',
'radii':r'$r$',
'pt':r'$\mathrm{log}(p_{T})$',
'eta':r'$\eta$',
'phi':r'$\phi$',
'mass':r'Mass',
'tau1':r'$\tau_{1}$',
'tau2':r'$\tau_{2}$',
}


def printTime(delta, returnString= False):
    
    h = (delta // 3600)
    m = (delta % 3600) // 60
    s = delta % 60
    
    if (delta > 3600):
        timestring = 'Time {0:.0f}h {1:.0f}m {2:.2f}s'.format(h, m, s)
        
    elif (delta > 60):
        timestring = 'Time {0:.0f}m {1:.2f}s'.format(m, s)
    
    else:
        timestring = 'Time {0:.2f}s'.format(s)
        
        
    if(returnString):
        return timestring
    else:
        print(timestring)
        
        
        
def plotFeature(X, Y, feat, alpha):
    
    siglab = Y[:,1]==1
    bkglab = Y[:,1]==0
    
    
    
    sig = X[feat][siglab].flatten()
    bkg = X[feat][bkglab].flatten()
    
    maximum = np.max([np.max(sig), np.max(bkg)])
    minimum = np.min([np.min(sig), np.min(bkg)])
    nbins = 50
    brange = np.linspace(minimum, maximum, 50)
    
    
    plt.hist(sig, bins=brange, hatch='//', alpha=alpha, label='Signal', density=True)
    plt.hist(sig, bins=brange, histtype='step', color='k', density=True)
    plt.hist(bkg, bins=brange, hatch='\\\\', alpha=alpha, label='Background', density=True)
    plt.hist(bkg, bins=brange, histtype='step', color='k', density=True)
    
    plt.xlabel(xlabels[feat])
    plt.ylabel('Density')
    
    plt.legend()
    plt.show()     
        
        
        
def getAdversary(X, X_shift, Y):

    xval = X.flatten()
    xval_s = X_shift.flatten()

    maximum = np.max([np.max(X), np.max(X_shift)])
    minimum = np.min([np.min(X), np.min(X_shift)])
    nbins = 50
    brange = np.linspace(minimum, maximum, 50)

    hx = plt.hist(xval, bins=brange, histtype='step', color='k', label=r'$\Delta \theta$', density=True)
    hxs = plt.hist(xval_s, bins=brange, histtype='step', color='darkgray', label=r'Perturbed $\Delta \theta$', density=True)
    plt.xlabel(xlabels['theta'])
    plt.ylabel('Density')
    plt.legend()
    plt.show()
    
    hx_height = hx[0]
    hxs_height = hxs[0]
    height = hx_height-hxs_height
    xaxis = hx[1][1:]
   
    plt.plot(xaxis, height, color='k', linewidth=2, label='Adversary')
    plt.xlabel(xlabels['theta'])
    plt.ylabel('Density')
    plt.legend()
    
    label_adv = np.ones_like(height)

    plt.show()
    
    
    return height, label_adv        
        
        
def plotBin(nBin, xvar, predictions, rows, cols, ax):
    
    print('plotting bin {}'.format(nBin))
    
    ycol = ((nBin-1) % cols)
    xrow = int(np.floor((nBin-1) // cols))
    
    ax[xrow][ycol].scatter(xvar, predictions[:,nBin-1])
    ax[xrow][ycol].set_xlabel(r'$\Delta \theta$')
    ax[xrow][ycol].set_ylabel(r'Prediction')
    ax[xrow][ycol].set_title('Bin '+str(nBin))
    ax[xrow][ycol].set_ylim([0,1])
    
    
        
def get_prediction_yvalues(xvar, predictions, norm=False, nBins=10):
    
    bmin = np.min(xvar)
    bmax = np.max(xvar)
    brange = np.linspace(bmin, bmax, nBins+1)
    
    mean, bin_edges, bins = stats.binned_statistic(xvar, predictions, statistic='mean', bins=brange, range=(bmin, bmax))
    sums, _, _ = stats.binned_statistic(xvar, predictions, statistic='sum', bins=brange, range=(bmin, bmax))
    yerr, _, _ = stats.binned_statistic(xvar, predictions, statistic='std', bins=brange, range=(bmin, bmax))
    
    # get bin centers
    bin_width = (bin_edges[1] - bin_edges[0])
    xvals = bin_edges[1:] - bin_width/2
    
    hmax = np.max(sums)
    
    yerr = np.sqrt(sums)
    
    if(norm):
        
        yvals = mean
        
        yerr = np.divide(yerr, sums)
        
    else:
        
        yvals = sums
        
        
    
    return xvals, yvals, yerr



