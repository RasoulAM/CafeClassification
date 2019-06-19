# Text Classification on Persian Text with BERT using Google Colab

## Introduction
This notebook can be used to run text classification on Persian text. It is meant to be run on [Google colab](colab.research.google.com) which is a free cloud service by Google that provides you with a jupyter notebook that can be run on a free CPU or GPU.

## Functionality Explained

This notebook fine tunes the bert multilingual model which has been pretrained on the Persian Wikipedia Corpus. You can download the different models [here](github.com/google-research/bert).
The model we used in this notebook is [multilingual_L-12_H-768_A-12](https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip)
After fine tuning based on the classification task, test results are infered with the resulting network.

## How to use this notebook

The data that will be used has to be on a google drive. The notebook is configured to read the data from a google drive of your choice and writes the results to the same drive. This is neccessary because colab discards everything when your session ends (basically when you close your browser or when your internet connection fails). So whenever you want to start training, make sure you can staty connected for enough time.

## A bit on colab
Using colab is a bit tricky! Your runtime and session is connected as long as your broswer is open and connected to the internet. Whenever you get disconnented, your session is discarded.

## Resource Consumption

This script uses up 6 to 8 Gigabytes of GPU RAM. The amount of data effects the amount of RAM that is used.
Have these numbers in mind before trying to fine tune a bert model locallly.


## Results

We used this notebook for running text classification on the Divar posts dataset. (part of this dataset can be found [here](https://research.cafebazaar.ir/visage/datasets/)) The posts in this dataset came from 10 different categories.

Dataset size | GPU RAM usage   |  Training time | Accuracy
-------------| :-------------: | :------------: | :----------------:
100k         |  7.0 G          |  1h            | 92.82
200k         |  7.6 G          |  2h            | 93.84
500k         |  7.8 G          |  6h            | 94.68