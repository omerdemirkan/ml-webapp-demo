import tensorflow as tf
import numpy as np
from datetime import datetime
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.callbacks import TensorBoard
from generator import ImgGenFromDir

vgg16_model = VGG16(include_top=False, input_shape=(224, 224, 3))

model = Sequential()
for layer in vgg16_model.layers:
    model.add(layer)

for layer in model.layers:
    layer.trainable = False

model.add(Flatten())
model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(1, activation='sigmoid'))

train_gen = ImgGenFromDir("data/train", 224, 32)
valid_gen = ImgGenFromDir("data/valid", 224, 32)

timestr = datetime.now().strftime("%Y-%m-%d-%H-%M")
tensorboard = TensorBoard(log_dir=f"models/logs/VGG16-{timestr}")

opt = SGD(lr=0.001, momentum=0.9)
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x=train_gen, validation_data=valid_gen, epochs=10, callbacks=[tensorboard])
model.save(f"VGG16-{timestr}.model")
