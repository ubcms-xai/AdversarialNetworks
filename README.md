# AdversarialNetworks
Using adversarial networks to reduce uncertainties or look for BSM physics



## Tests and Tutorials

You will need to run this in the **srappoccio/ubccr-cms:latest** docker image. 

## (Optional) Log into winterfell (every time)

Open a terminal and ssh to winterfell: 

```
ssh -i ~/(yourpemfile).pem (yourusername)@199.109.192.91
```

If you've set up your account correctly, if you type `pwd` you should see `/mnt/users/(yourusername)`. 



## Set up a working directory (do once)

Make a directory for your work. Make sure it has write access: 

```
mkdir dockers
chmod 777 dockers
```

Clone the package:

```
git clone https://github.com/ubcms-xai/AdversarialNetworks.git
chmod -R 777 AdversarialNetworks
```

Make a data directory:

```
cd AdversarialNetworks
mkdir data
chmod -R 777 .
```

## Run the docker image and jupyter notebook (do every time)

Start the docker image. You may have to change the port from 8888 to something else like 8883, 8884, etc. 

``` 
bash ./runDockerCommandLine.sh 8888 srappoccio/ubccr-cms:latest
```


Start a jupyter notebook:

```
jupyter notebook --ip 0.0.0.0 --no-browser
```

## Run the code

Then you can begin running the code.

1. Open `ToyModel/makeFourVectors.ipynb`
2. Click "Run"
3. Change `addPerturbation = True` to `addPerturbation = False`
4. Click "Run" again
5. Open `ToyModel/toy_adversarial_1dcnn.ipynb`
6. Click "Run"

