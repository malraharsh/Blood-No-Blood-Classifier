import argparse
import os
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import zipfile
 
from sklearn.metrics import (accuracy_score, classification_report,confusion_matrix)
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.layers import (AveragePooling2D, Dense, Dropout, Flatten, Input, MaxPooling2D)
from tensorflow.keras.models import Model, load_model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import (ImageDataGenerator,img_to_array, load_img)
from tensorflow.keras.utils import to_categorical

def getFiles(path):
    return ([os.path.join(path, p) for p in os.listdir(path)])

def getCorrupted(df):
    corrupted = []
    for impath in df.files:
        try:
            plt.imread(impath)
        except:
            corrupted.append(impath)
    return corrupted
            
def removeCorrupted(df, corrupted):
    todrop = df[[f in corrupted for f in df['files']]].index
    print("Removed {}".format(len(corrupted)))
    return df.drop(todrop)

def get_model():
    base = MobileNetV2(input_tensor=Input(shape=(224, 224,3)), weights="imagenet", include_top=False)
    model = Sequential()
    model.add(base)
    model.add(MaxPooling2D(pool_size=(5, 5)))
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(1, activation="sigmoid"))

    base.trainable = False

    optimizer = Adam(lr=1e-4)
    model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])
    return model