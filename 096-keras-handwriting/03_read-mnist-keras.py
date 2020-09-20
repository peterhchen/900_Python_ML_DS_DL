from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = \
    mnist.load_data()
print('mnist_train_images.shape:')
print(mnist_train_images.shape)   # (60000, 28, 28)
print('mnist_train_labels.shape:')
print(mnist_train_labels.shape) # (60000,)
print('mnist_test_images.shape:')
print(mnist_test_images.shape)  # (10000, 28, 28):
print('mnist_test_labels.shape:')
print(mnist_test_labels.shape)  # (10000,)
