import numpy as np
import os
import random

#load cat image paths
cat_paths = []
for file in os.listdir("data\\train\\Cat"):
    cat_paths.append(os.path.join("data\\train\\Cat", file))

#load dog image paths
dog_paths = []
for file in os.listdir("data\\train\\Dog"):
    dog_paths.append(os.path.join("data\\train\\Dog", file))

#shuffle paths
random.shuffle(cat_paths)
random.shuffle(dog_paths)

#split training and validation data
cat_paths_valid = cat_paths[:round(len(cat_paths) * 0.1)]
dog_paths_valid = dog_paths[:round(len(dog_paths) * 0.1)]

#move cats to validation directory
for file in cat_paths_valid:
    filename = file.split("\\")[-1]
    os.rename(file, os.path.join("data\\valid\\Cat", filename))

#move dogs to validation directory
for file in dog_paths_valid:
    filename = file.split("\\")[-1]
    os.rename(file, os.path.join("data\\valid\\Dog", filename))
