from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = \
    mnist.load_data()

# print('mnist_train_images.shape:')
# print(mnist_train_images.shape)   # (60000, 28, 28)
# print('mnist_train_labels.shape:')
# print(mnist_train_labels.shape) # (60000,)
# print('mnist_test_images.shape:')
# print(mnist_test_images.shape)  # (10000, 28, 28):
# print('mnist_test_labels.shape:')
# print(mnist_test_labels.shape)  # (10000,)

train_images = mnist_train_images.reshape(60000, 784)
test_images = mnist_test_images.reshape(10000, 784)
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')

def print_image (param):
    print(param)
    i = 0
    for x in train_images:
        if i < 1:
            print ('x[250:350]:')
            print (x[250:350])
        else:
            break
        i += 1

# print_image('before scale:')
train_images /= 255
test_images /= 255
# print_image('after scale:')

def print_one_hot_label (name, param):
    print(name)
    for x in param:
        print (x)

train_labels = keras.utils.to_categorical(mnist_train_labels, 10)
test_labels = keras.utils.to_categorical(mnist_test_labels, 10)

print_one_hot_label ('mnist_train_labels:', mnist_train_labels[:5])
print_one_hot_label ('train_labels:', train_labels[:5])