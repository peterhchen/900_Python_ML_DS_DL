# Prepare MNIST data.
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# MNIST dataset parameters
num_classes = 10 # total classes (0-9 digits)
num_features = 784 # data features (img shape: 28*28)

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print ('mnist=>x_train[:1][:1][:1]:', x_train[:1][:1][:1])
# print ('mnist=>y_train[:1][:1]:', y_train[:1][:5])
# print ('mnist=>x_test[:1]:', x_test[:1])
# print ('mnist=>y_test[:1]:',  y_test[:1])

# Convert to float32
x_train, x_test = np.array(x_train, np.float32), np.array(x_test, np.float32)
# print ('\nconvert to float32=>x_train[:1]:', x_train[:1])
# print ('convert to float32 =>x_test[:1]:', x_test[:1])

# Flatten images to 1-D vector of 784 features (28*28)
x_train, x_test = x_train.reshape([-1, num_features]), x_test.reshape([-1, num_features])
# print ('\n1-D vector to 784 features (28*28)=>x_train[:1]:', x_train[:1])
# print ('1-D vector to 784 features (28*28) =>x_test[:1]:',  x_test[:1])

# Normalize images value from [0, 255] to [0, 1]
x_train, x_test = x_train / 255., x_test / 255.
# print('Normalize images value from [0, 255] to [0, 1] => x_train[:1]:')
# print(x_train[:1])
# print('Normalize images value from [0, 255] to [0, 1] => x_test[:1]:')
# print(x_test[:1])
# print('y_train[:1]:', y_train[:1])
# print('y_test[:1]:', y_test[:1])

import matplotlib.pyplot as plt

def display_sample(num):
    #Print this sample's label 
    label = y_train[num] 
    
    #Reshape the 784 values to a 28x28 image
    image = x_train[num].reshape([28,28])
    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()
    
# display_sample(5)
# display_sample(50)
# display_sample(500)
# display_sample(5000)
# display_sample(50000)
# display_sample(59999)

images = x_train[0].reshape([1,784])
for i in range(1, 500):
    images = np.concatenate((images, x_train[i].reshape([1,784])))
plt.imshow(images, cmap=plt.get_cmap('gray_r'))
plt.show()