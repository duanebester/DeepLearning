# DeepLearning
Deep Learning Experiments


### Image Fixer

#### Setup

```
cd image-fixer
```

Image data for image-fixer project: https://www.dropbox.com/s/d096vkzvdvrm3az/raw.zip?dl=0

Extract image data

Then create training folders:

```
mkdir -p data/trainA
mkdir -p data/trainB
mkdir -p data/testA
mkdir -p data/testB
```

Python deps

```
pip install -r requirements.txt
```

##### Data Generation

Update project directory in `data_generation.py`:

```
project_directory = r'/Users/duanebester/code/DeepLearning/image-fixer/'
```

This takes our raw images and creates more images using Keras' ImageDataGenerator

```
python3 data_generation.py
```

##### Data Prep

This takes our generated images and sorts them into test and train directories, as well as saving them as a numpy data array: data_256.npz

```
python3 data_preparation.py
```

##### Data Prep Plotting

This just plots our prepped data for sanity checking

```
python3 data_prep_plot.py
```

##### Training

Running our training

```
python3 train.py
```