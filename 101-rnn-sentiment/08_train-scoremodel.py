from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.datasets import imdb

print('Loading data...')
(x_train, y_train), (x_test, y_test) = \
    imdb.load_data(num_words=20000)

# print('x_train[0]:')
# print(x_train[0])
# print('y_train[0]:')
# print(y_train[0])

# Pick up the first 80 words in training data.
x_train = sequence.pad_sequences(x_train, maxlen=80)
x_test = sequence.pad_sequences(x_test, maxlen=80)
# print('Limit Train/Test data length =>x_train[0]:')
# print(x_train[0])

# Setup LSTM (Lng Short-Term Model) for RNN Model
model = Sequential()
model.add(Embedding(20000, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# Compile Model
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Train Model
model.fit(x_train, y_train,
          batch_size=32,
          epochs=15,
          verbose=2,
          validation_data=(x_test, y_test))

# score model
score, acc = model.evaluate(x_test, y_test,
                            batch_size=32,
                            verbose=2)
print('Test score:', score)
print('Test accuracy:', acc)