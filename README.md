# AdversarialNetworks
Using adversarial networks to reduce uncertainties or look for BSM physics



## Run Adapted Particle Net Code

You will need to run this in two separate docker images:

**srappoccio/innvestigate_tensorflow:latest** and **srappoccio/ubccr-cms:latest**

To run with two separate dockers, make two directories:



``mkdir AdversarialNetworks_innvestigate_tensorflow``

``cd AdversarialNetworks_innvestigate_tensorflow``

``git clone https://github.com/ubcms-xai/AdversarialNetworks.git``

``docker pull srappoccio/innvestigate_tensorflow:latest``

Make another directory for the ubccr-cms docker:

``cd ../``

``mkdir AdversarialNetworks_ubccr-cms``

``cd AdversarialNetworks_ubccr-cms``

``git clone https://github.com/ubcms-xai/AdversarialNetworks.git``

``docker pull srappoccio/ubccr-cms:latest``


Then you can begin running the code.



First run  ``convert_dataset.ipynb`` and ``keras_train__docker_innvestigate_tensorflow.ipynb`` in the **innvestigate_tensorflow** docker image.

If you are not running on Winterfell (most of you), you will have to download the .h5 files that ``convert_dataset.ipynb`` is converting. These are found here https://zenodo.org/record/2603256


### Code to run in investigate_tensorflow docker
1. convert_dataset.ipynb
2. keras_train__docker_innvestigate_tensorflow.ipynb

### Code to run in ubccr-cms docker
3. keras_train__docker_ubccr-cms.ipynb



