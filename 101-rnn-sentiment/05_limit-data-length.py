from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.datasets import imdb

print('Loading data...')
(x_train, y_train), (x_test, y_test) = \
    imdb.load_data(num_words=20000)

print('x_train[0]:')
print(x_train[0])
# print('y_train[0]:')
# print(y_train[0])

# Pick up the first 80 words in training data.
x_train = sequence.pad_sequences(x_train, maxlen=80)
x_test = sequence.pad_sequences(x_test, maxlen=80)
print('Limit Train/Test data length =>x_train[0]:')
print(x_train[0])