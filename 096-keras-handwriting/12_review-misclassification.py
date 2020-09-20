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

# print_one_hot_label ('mnist_train_labels:', mnist_train_labels[:5])
# print_one_hot_label ('train_labels:', train_labels[:5])

import matplotlib.pyplot as plt

def display_sample(num):
    #Print the one-hot array of this sample's label 
    print(train_labels[num])  
    #Print the label converted back to a number
    label = train_labels[num].argmax(axis=0)
    #Reshape the 768 values to a 28x28 image
    image = train_images[num].reshape([28,28])
    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()
    
#display_sample(1234)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

print(model.summary())

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels,
                    batch_size=100,
                    epochs=10,
                    verbose=2,
                    validation_data=(test_images, test_labels))

# Evaluate Model
score = model.evaluate(test_images, test_labels, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Review Misclassified
for x in range(1000):
    test_image = test_images[x,:].reshape(1,784)
    predicted_cat = model.predict(test_image).argmax()
    label = test_labels[x].argmax()
    if (predicted_cat != label):
        plt.title('Prediction: %d Label: %d' % (predicted_cat, label))
        plt.imshow(test_image.reshape([28,28]), cmap=plt.get_cmap('gray_r'))
        plt.show()