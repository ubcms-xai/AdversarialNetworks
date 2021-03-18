# AdversarialNetworks
Using adversarial networks to reduce uncertainties or look for BSM physics



## Tests and Tutorials

You will need to run this in the **srappoccio/ubccr-cms:latest** docker image. 



Make another directory for the ubccr-cms docker:

```
git clone https://github.com/ubcms-xai/AdversarialNetworks.git
docker pull srappoccio/ubccr-cms:latest
bash ./runDockerCommandLine.sh 8889 srappoccio/ubccr-cms:latest
```


Start a jupyter notebook:

```
cd /home/physicist
jupyter notebook --ip 0.0.0.0 --no-browser
```

Then you can begin running the code.

1. Open `ToyModel/makeFourVectors.ipynb`
2. Click "Run"
3. Open `ToyModel/toy_adversarial_1dcnn.ipynb`
4. Click "Run"

