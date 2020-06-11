# %%
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

from utils import *

label_list = ['W', 'A', 'S', 'D',
              'WA', 'WD', 'SA', 'SD',
              'AW', 'DW', 'AS', 'DS',  '']

def generate_sample(batch_size, filepath):

    filenames = dir_file(filepath)
    while 1:
        index_file = np.random.choice(len(filenames), len(filenames), replace=False)
        shuffled_filenames = []
        for indx in index_file:
            shuffled_filenames.append(filenames[indx])
        steps_per_epoch = len(filenames) // batch_size

        imgs = np.zeros((batch_size, 150, 200, 1))
        targets = np.zeros((batch_size, 1))
        for step in range(steps_per_epoch):
            batch_filenames = shuffled_filenames[step * batch_size:(step + 1) * batch_size]
            for i in range(batch_size):
                data = cv2.imread(filepath + batch_filenames[i], flags=cv2.IMREAD_GRAYSCALE)
                data = data/np.max(data)
                imgs[i] = data[:, :, np.newaxis]
                label = get_label(batch_filenames[i])
                targets[i] = label_list.index(label)
            yield (imgs, targets)

# %%

if __name__ == "__main__":

    filepath = 'E:/GAME/GTA5/data/'
    gen = generate_sample(128, filepath)
    for x, y in gen:
        plt.imshow(x[0, :, :, 0], cmap='gray')
        plt.show()
# %%
