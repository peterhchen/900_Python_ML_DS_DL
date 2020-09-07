import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
#print('iris:')
#print(iris) # {'data': array([[5.1, 3.5, 1.4, 0.2], ...
print("iris['data'][:5]:")
print(iris['data'][:5])

# Split the iris data into train/test data sets 
# with 40% reserved for testing
X_train, X_test, y_train, y_test = \
    train_test_split(iris.data, iris.target, \
    test_size=0.4, random_state=0)

# Build an SVC model for predicting iris 
# classifications using training data
# clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
# degree = 3
clf = svm.SVC(kernel='poly', degree=3, C=1).fit(X_train, y_train)

# Now measure its performance with the test data
clf.score(X_test, y_test)   

# Now measure its performance with the test data
# clf.score(X_test, y_test)
print ('\nSVC(Support Vector Classifier):')
print ('clf.score(X_test, y_test):')
print (clf.score(X_test, y_test))

# We give cross_val_score a model, the entire data 
# set and its "real" values, and the number of folds:
# Set K = 5 (cv = 5)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)

# Print the accuracy for each fold:
print('\nK-Fold Cross Validation:')
print('scores:')
print(scores)

# And the mean accuracy of all 5 folds:
print('scores.mean():')
print(scores.mean())
