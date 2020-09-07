import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
#print('iris:')
#print(iris) # {'data': array([[5.1, 3.5, 1.4, 0.2], ...
print("iris['data'][:5]:")
print(iris['data'][:5])

# Split the iris data into train/test data sets with 40% reserved for testing
X_train, X_test, y_train, y_test = \
    train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

# Build an SVC model for predicting iris classifications using training data
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)

# Now measure its performance with the test data
#clf.score(X_test, y_test)
print ('\nclf.score(X_test, y_test):')
print (clf.score(X_test, y_test))   