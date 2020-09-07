import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
#print('iris:')
#print(iris) # {'data': array([[5.1, 3.5, 1.4, 0.2], ...
print("iris['data'][:5]:")
print(iris['data'][:5])