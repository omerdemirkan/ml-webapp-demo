import cv2
import os
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("model/models/VGG16-2020-02-26-17-44.model")

def predict_path(path):
    if not os.path.exists(path):
        print(f"{path} is an invalid path.")

    img_arr = cv2.imread(path, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_arr, (224, 224))
    img_resized = img_resized.astype(np.float32) / 255.0

    return model.predict(np.array([img_resized]))[0][0]

def predict_img():
    return None