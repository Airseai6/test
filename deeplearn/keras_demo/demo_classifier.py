#! python3
# -*- coding:utf-8 -*-

import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
np.random.seed(1337)  # for reproducibility


# download the mnist to the path './keras/datasets/' if it is the first time to be called
# X shape(60,000 28*28), Y shape(10,000, )
(X_train, Y_train),  (X_test, Y_test) = mnist.load_data()

# data pre-processing
X_train = X_train.reshape(X_train.shape[0], -1)/255  # normalize
X_test = X_test.reshape(X_test.shape[0], -1)/255  # normalize
Y_train = np_utils.to_categorical(Y_train, num_classes=10)
Y_test = np_utils.to_categorical(Y_test, num_classes=10)

# Another way to build your neural net
model = Sequential([
    Dense(32, input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax')
])

# Another way to define your optimizer
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

# We add metrics to get more results your want to see
model.compile(
    loss='categorical_crossentropy',
    optimizer=rmsprop,
    metrics=['accuracy'],
)


print('Training~~~~~~~~~~')
# Another way to train the model
model.fit(X_train, Y_train, epochs=2, batch_size=32)


print('\nTesting~~~~~~~~~')
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(X_test, Y_test)
print('test loss: ', loss, '\ntest accuracy: ', accuracy)
