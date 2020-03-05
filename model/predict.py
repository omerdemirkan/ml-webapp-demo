import os
import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("model/models/VGG16-2020-02-26-17-44.model")

def predict(img_arr):
    #resize and normalize image before prediction
    img_arr = cv2.resize(img_arr, (224, 224))
    img_arr = img_arr.astype(np.float32) / 255.0

    return model.predict(np.array([img_arr]))[0][0]