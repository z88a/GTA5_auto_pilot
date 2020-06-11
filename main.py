# %%
import keras
import matplotlib.pyplot as plt
import numpy as np

from net import net
from sample_generator import generate_sample

# %% 
# parameter config
batch_size = 64
learning_rate = 0.001
l2_regularizer = 0.0001
dropout_rate = 0.2
epochs = 100

filepath = 'E:/GAME/GTA5/data/'
filenames = dir(filepath)
steps_per_epoch = len(filenames) // batch_size

# %%
# model
model = net((150, 200, 1), 13)
model.summary()
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=keras.optimizers.Adam(lr=learning_rate),
              metrics=['acc'])
# %% 
# Train step
train_gen = generate_sample(batch_size, filepath)
hist = model.fit_generator(train_gen, steps_per_epoch=steps_per_epoch, epochs=epochs)

# %%
plt.plot(hist.history['acc'])

