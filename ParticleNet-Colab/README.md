# Run in Google Colab

Go to https://colab.research.google.com/

Select 'Github' and enter the github link. The files in this repository should appear.

In order to for a notebook use files created by another notebook, you will have to mount your google drive to google colab for each notebook that you are running (the code is already set up to do this)

1. Run convert_dataset.ipynb. This will create new directories in your google drive but you need to upload the train.h5, test.h5, and val.h5 to run the last 4 cells
2. Run keras_train.ipynb, which will load the converted files

