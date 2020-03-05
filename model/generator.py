import cv2
import os
import numpy as np
from tensorflow.keras.utils import Sequence

class ImgGenFromDir(Sequence):
    def __init__(self, dir, img_size, batch_size):
        #populate paths and labels from dir
        self.paths = []
        self.labels = []
        for subdir in os.listdir(dir):
            category_path = os.path.join(dir, subdir)
            for file in os.listdir(category_path):
                self.paths.append(os.path.join(category_path, file))
                if subdir == 'Cat':
                    self.labels.append(1)
                else:
                    self.labels.append(0)

        #convert paths and labels to arrays
        self.paths = np.array(self.paths)
        self.labels = np.array(self.labels)

        #shuffle paths and labels together
        indicies = np.arange(self.paths.shape[0])
        np.random.shuffle(indicies)
        self.paths = self.paths[indicies]
        self.labels = self.labels[indicies]

        self.img_size = img_size
        self.batch_size = batch_size

    def __len__(self):
        return np.ceil(len(self.paths) / float(self.batch_size)).astype(np.int)

    def __getitem__(self, i):
        #load paths and labels for current batch
        paths = self.paths[i * self.batch_size: (i+1) * self.batch_size]
        labels = self.labels[i * self.batch_size: (i+1) * self.batch_size]

        #load images
        batch_features = []
        batch_labels = []
        for i in range(len(paths)):
            try:
                img_arr = cv2.imread(paths[i], cv2.COLOR_BGR2RGB)
                img_resized = cv2.resize(img_arr, (self.img_size, self.img_size))
                if img_resized.shape == (self.img_size, self.img_size, 3):
                    batch_features.append(img_resized)
                    batch_labels.append(labels[i])
            except Exception as e:
                pass

        #convert batch_features, batch_labels to arrays
        batch_features = np.array(batch_features)
        batch_labels = np.array(batch_labels)

        #normalize images
        batch_features = batch_features.astype(np.float32)
        batch_features /= 255.0

        return batch_features, batch_labels
