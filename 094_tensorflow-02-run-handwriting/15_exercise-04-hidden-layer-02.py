# Prepare MNIST data.
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# MNIST dataset parameters
num_classes = 10 # total classes (0-9 digits)
num_features = 784 # data features (img shape: 28*28)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Convert to float32
x_train, x_test = np.array(x_train, np.float32), np.array(x_test, np.float32)


# Flatten images to 1-D vector of 784 features (28*28)
x_train, x_test = x_train.reshape([-1, num_features]), x_test.reshape([-1, num_features])


# Normalize images value from [0, 255] to [0, 1]
x_train, x_test = x_train / 255., x_test / 255.


import matplotlib.pyplot as plt

def display_sample(num):
    #Print this sample's label 
    label = y_train[num] 
    
    #Reshape the 784 values to a 28x28 image
    image = x_train[num].reshape([28,28])
    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()
    

images = x_train[0].reshape([1,784])
for i in range(1, 500):
    images = np.concatenate((images, x_train[i].reshape([1,784])))
# plt.imshow(images, cmap=plt.get_cmap('gray_r'))
# plt.show()

# Training parameters.
learning_rate = 0.001
training_steps = 3000
batch_size = 250
display_step = 100

# Network parameters.
n_hidden1 = 512 # Number of neurons of hidden layer 1.
n_hidden2 = 512 # Number of neurons of hidden layer 2.

# Use tf.data API to shuffle and batch data.
train_data = tf.data.Dataset.from_tensor_slices((x_train, y_train))

train_data = train_data.repeat().shuffle(60000).batch(batch_size).prefetch(1)
# print('shuffle => train_data[:5]:')
# print(train_data)

# Store layers weight & bias

# A random value generator to initialize weights initially
random_normal = tf.initializers.RandomNormal()

weight1 = {
    'h1': tf.Variable(random_normal([num_features, n_hidden1])),
    'out': tf.Variable(random_normal([n_hidden1, num_classes]))
}
weight2 = {
    'h2': tf.Variable(random_normal([n_hidden1, n_hidden2])),
    'out': tf.Variable(random_normal([n_hidden2, num_classes]))
}

bias1 = {
    'b': tf.Variable(tf.zeros([n_hidden1])),
    'out': tf.Variable(tf.zeros([num_classes]))
}

bias2 = {
    'b': tf.Variable(tf.zeros([n_hidden2])),
    'out': tf.Variable(tf.zeros([num_classes]))
}

# Create model.
def neural_net(inputData):
    # Hidden fully connected layer with 512 neurons.
    # output = input * weight + bias
    # print ('inputData.shape1:', inputData.shape)        # (250, 748)
    # print ("weight1['h1'].shape1:", weight1['h1'].shape)    # (748, 512)
    # print ("bias1['b'].shape1:", bias1['b'].shape)           # (748, 512)
    hidden_layer1 = tf.add(tf.matmul(inputData, weight1['h1']), bias1['b'])
    # print ('hidden_layer1.shape2:', hidden_layer1.shape)
    # print ("weight2['h2'].shape2:", weight2['h2'].shape)
    # matrix size incompatible: In[0]: [250, 1024], In[1]: [748, 1024]
    hidden_layer2 = tf.add(tf.matmul(hidden_layer1, weight2['h2']), bias2['b'])
    # hidden_layer = tf.add(tf.matmul(inputData, weights['h']), biases['b'])
 
    # Apply sigmoid to hidden_layer output for non-linearity.
    hidden_layer = tf.nn.sigmoid(hidden_layer2)
    #hidden_layer = tf.nn.sigmoid(hidden_layer1)
    
    # Output fully connected layer with a neuron for each class.
    out_layer = tf.matmul(hidden_layer2, weight2['out']) + bias2['out']
    # Apply softmax to normalize the logits to a probability distribution.
    return tf.nn.softmax(out_layer)

def cross_entropy(y_pred, y_true):
    # Encode label to a one hot vector.
    y_true = tf.one_hot(y_true, depth=num_classes)
    # Clip prediction values to avoid log(0) error.
    y_pred = tf.clip_by_value(y_pred, 1e-9, 1.)
    # Compute cross-entropy.
    return tf.reduce_mean(-tf.reduce_sum(y_true * tf.math.log(y_pred)))

optimizer = tf.keras.optimizers.SGD(learning_rate)

def run_optimization(x, y):
    # Wrap computation inside a GradientTape for automatic differentiation.
    with tf.GradientTape() as g:
        pred = neural_net(x)
        loss = cross_entropy(pred, y)
        
    # Variables to update, i.e. trainable variables.
    trainable_variables = list(weight2.values()) + list(bias2.values())

    # Compute gradients.
    gradients = g.gradient(loss, trainable_variables)
    
    # Update W and b following gradients.
    optimizer.apply_gradients(zip(gradients, trainable_variables))

# Accuracy metric.
def accuracy(y_pred, y_true):
    # Predicted class is the index of highest score in prediction vector (i.e. argmax).
    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.cast(y_true, tf.int64))
    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32), axis=-1)

# Run training for the given number of steps.
for step, (batch_x, batch_y) in enumerate(train_data.take(training_steps), 1):
    # Run the optimization to update W and b values.
    run_optimization(batch_x, batch_y)
    
    if step % display_step == 0:
        pred = neural_net(batch_x)
        loss = cross_entropy(pred, batch_y)
        acc = accuracy(pred, batch_y)
        print("Training epoch: %i, Loss: %f, Accuracy: %f" % (step, loss, acc))

# Test model on validation set.
pred = neural_net(x_test)
print("Test Accuracy: %f" % accuracy(pred, y_test))

# n_images = 200
# test_images = x_test[:n_images]
# test_labels = y_test[:n_images]
# predictions = neural_net(test_images)

# for i in range(n_images):
#     model_prediction = np.argmax(predictions.numpy()[i])
#     if (model_prediction != test_labels[i]):
#         plt.imshow(np.reshape(test_images[i], [28, 28]), cmap='gray_r')
#         plt.show()
#         print("Original Labels: %i" % test_labels[i])
#         print("Model prediction: %i" % model_prediction)
