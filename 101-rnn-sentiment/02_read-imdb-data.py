from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.datasets import imdb

print('Loading data...')
(x_train, y_train), (x_test, y_test) = \
    imdb.load_data(num_words=20000)
