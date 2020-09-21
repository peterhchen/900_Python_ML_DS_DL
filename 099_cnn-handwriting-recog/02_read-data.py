import tensorflow
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import RMSprop

(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) \
    = mnist.load_data()
print('mnist_train_images.shape:')
print(mnist_train_images.shape)
print('mnist_train_labels.shape')
print(mnist_train_labels.shape)