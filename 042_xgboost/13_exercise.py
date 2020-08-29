# Read iris data set
from sklearn.datasets import load_iris

iris = load_iris()

numSamples, numFeatures = iris.data.shape
print('numSamples:', numSamples)
print('numFeatures:', numFeatures)
print('list(iris.target_names):')
print(list(iris.target_names))

# Split the data into Train and Test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = \
    train_test_split (iris.data, iris.target, \
    test_size=0.2, random_state=0)

import xgboost as xgb

train = xgb.DMatrix(X_train, label=y_train)
test = xgb.DMatrix(X_test, label=y_test)

print('train:', train)
print ('test:', test)

# Define Hyperparameter
param = {
    'max_depth': 2,
    'eta': 0.5,
    'objective': 'multi:softmax',
    'num_class': 3} 
epochs = 5
# Train Model
model = xgb.train(param, train, epochs)
# Make Predcition
predictions = model.predict(test)
print('predictions:')
print(predictions)

# Measure accuracy
from sklearn.metrics import accuracy_score
print ('accuracy_score(y_test, predictions)):')
print (accuracy_score(y_test, predictions))
