# -*- coding: utf-8 -*-
"""vgg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13lUMBdeePIkD_KMJ424zSmmLFoaz0mjH
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers import Conv3D, MaxPooling3D

def VGG16_3D(input_shape, classes=1000):
    model = Sequential(name='VGG19 3D')
    # Block 1
    model.add(Conv3D(input_shape=input_shape,
                     filters=64,
                     kernel_size=(3,3,3),
                     padding='same',
                     activation='relu',
                     name='block1_conv1'))
    model.add(Conv3D(filters=64,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block1_conv2'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name='block1_pool'))
    # Block 2
    model.add(Conv3D(filters=128,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block2_conv1'))
    model.add(Conv3D(filters=128,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block2_conv2'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name'block2_pool'))
    # Block 3
    model.add(Conv3D(filters=256,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block3_conv1'))
    model.add(Conv3D(filters=256,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block3_conv2'))
    model.add(Conv3D(filters=256,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block3_conv3'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name'block3_pool'))
    # Block 4
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block4_conv1'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block4_conv2'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block4_conv3'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name'block4_pool'))
    
    # Block 5
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block5_conv1'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block5_conv2'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block5_conv3'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name'block5_pool'))
    
    model.add(Flatten(name='flatten'))
    model.add(Dense(units=4096,activation="relu",name='fc1'))
    model.add(Dense(units=4096,activation="relu",name='fc2'))
    model.add(Dense(units=classes, activation="softmax",name='predictions'))

    return model

def VGG19_3D(input_shape, classes=1000):
    model = Sequential(name='VGG19 3D')
    # Block 1
    model.add(Conv3D(input_shape=input_shape,
                     filters=64,
                     kernel_size=(3,3,3),
                     padding='same',
                     activation='relu',
                     name='block1_conv1'))
    model.add(Conv3D(filters=64,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block1_conv2'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name='block1_pool'))
    # Block 2
    model.add(Conv3D(filters=128,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block2_conv1'))
    model.add(Conv3D(filters=128,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block2_conv2'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name'block2_pool'))
    # Block 3
    model.add(Conv3D(filters=256,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block3_conv1'))
    model.add(Conv3D(filters=256,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block3_conv2'))
    model.add(Conv3D(filters=256,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block3_conv3'))
    model.add(Conv3D(filters=256,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block3_conv4'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name'block3_pool'))
    # Block 4
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block4_conv1'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block4_conv2'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block4_conv3'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block4_conv4'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name'block4_pool'))
    
    # Block 5
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block5_conv1'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block5_conv2'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block5_conv3'))
    model.add(Conv3D(filters=512,
                     kernel_size=(3,3,3),
                     padding="same",
                     activation="relu",
                     name='block5_conv3'))
    model.add(MaxPooling3D(pool_size=(2,2,2),
                           strides=(2,2,2),
                           name'block5_pool'))
    
    model.add(Flatten(name='flatten'))
    model.add(Dense(units=4096,activation="relu",name='fc1'))
    model.add(Dense(units=4096,activation="relu",name='fc2'))
    model.add(Dense(units=classes, activation="softmax",name='predictions'))

    return model