#!/bin/bash

mkdir -p data/trainA
mkdir -p data/trainB
mkdir -p data/testA
mkdir -p data/testB

pip install -r requirements.txt

sudo pip install git+https://www.github.com/keras-team/keras-contrib.git

