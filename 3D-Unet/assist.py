import numpy as np
import os
import random
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm
import keras

name = 'npy_test'
path = '../' + name

def get_normalize(mean = [0.4914, 0.4822, 0.4465], std = [0.2023, 0.1993, 0.2010], to_Tensor=True):
    def normalizer(input_image):
        if to_Tensor:
            image = input_image / 255
        else:
            image = input_image

        reshape_shape = (1, 1, 3) if keras.backend.image_data_format() == 'channels_last' else (3, 1, 1)
        shaped_mean = np.reshape(mean, reshape_shape)
        shaped_std = np.reshape(std, reshape_shape)

        image = (image - shaped_mean) / shaped_std
        return image
    return normalizer


def image_label(imageLabel, label2idx, i):

    if imageLabel not in label2idx:
      label2idx[imageLabel]=i
      i=i+1
    return label2idx, i

def image2npy(dir_path='./imgs/', testScale = 0.1):

    i=0
    label2idx = {}
    data = []
    for (root, dirs, files) in os.walk(dir_path):
        for Ufile in tqdm(files):
            img_path = os.path.join(root, Ufile)
            File = root.split('/')[-1]

            img_data = cv2.imread(img_path)
            label2idx, i = image_label(File, label2idx, i)
            label = label2idx[File]

            data.append([np.array(img_data),label])

        random.shuffle(data)


        testNum = int(len(data)*testScale)
        train_data = data[:-1*testNum]
        test_data = data[-1*testNum:]

        x_train = np.array([i[0] for i in train_data])
        y_train = np.array([i[1] for i in train_data])

        x_test = np.array([i[0] for i in test_data])
        y_test = np.array([i[1] for i in test_data])

        print(len(x_train),len(y_train),len(x_test),len(y_test))

        dirs = os.path.join('npy_data',name)
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        np.save(os.path.join(dirs,'x_train'),x_train)
        np.save(os.path.join(dirs,'y_train'),y_train)
        np.save(os.path.join(dirs,'x_test'),x_test)
        np.save(os.path.join(dirs,'y_test'),y_test)

        return label2idx



label2idx = image2npy(dir_path=path, testScale=0.2)
print(label2idx)


image_no = np.random.randint(0, 100, size=9)  # 随机挑选9个数字

train_images = np.load(os.path.join('../npy_test/npy_data/'+name, 'x_train.npy'))
train_labels = np.load(os.path.join('../npy_test/npy_data/'+name, 'y_train.npy'))
fig, axes = plt.subplots(nrows=3, ncols=3,figsize=(7,7))

for i in range(3):
    for j in range(3):
        axes[i][j].imshow(train_images[image_no[i*3+j]])
        axes[i][j].set_title(train_labels[image_no[i*3+j]])
plt.tight_layout()
