import cv2
import os
import numpy as np
import tensorflow as tf
from base64 import b64decode

model = tf.keras.models.load_model("model/models/VGG16-2020-02-26-17-44.model")

def predict(img_data):
    img_arr = np.fromstring(b64decode(img_data), np.uint8)
    img_arr = cv2.imdecode(img_arr, cv2.COLOR_BGR2RGB)
    img_arr = cv2.resize(img_arr, (224, 224))
    img_arr = img_arr.astype(np.float32) / 255.0

    return model.predict(np.array([img_arr]))[0][0]