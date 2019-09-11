#! python3
# -*- coding:utf-8 -*-

'''
Deep Learning With Python book exercise
'''

# P51 电影二分类问题
# Code 1 load IMDB database
from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)


# Code 2 translate to matrix
import numpy as np


def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequences in enumerate(sequences):
        results[i, sequences] = 1
    return results


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')


# Code 3 define models
from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000, )))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

# # Code 4 compile the model
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# Code 5 to configure optimizer
from keras import optimizers

# model.compile(optimizer=optimizers.Rmsprop(lr=0.001), loss='binary_crossentropy',
#               metrics=['accuracy'])

# Code 6 use custom losses and metrics
from keras import losses
from keras import metrics

# model.compile(optimizers.RMSprop(lr=0.001),
#               loss=losses.binary_crossentropy,
#               metrics=[metrics.binary_accuracy])

# Code 7 keep out checking
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

# Code 8 train
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history = model.fit(partial_x_train, partial_y_train,  epochs=20, batch_size=512, validation_data=(x_val, y_val))

# Code 9 plot
import matplotlib.pyplot as plt

history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

epochs = range(1, len(loss_values)+1)
plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Code 10 plot train and checking
plt.clf()
acc = history_dict['acc']
val_acc = history_dict['val_acc']

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epches')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


