import pandas as pd

# masses_data = pd.read_csv('mammographic_masses.data.txt')
# print ('masses_data.head():')
# print (masses_data.head())

# Replace missing data (?) with NaN
# Add the first row with column name
masses_data = pd.read_csv('mammographic_masses.data.txt', na_values=['?'], \
    names = ['BI-RADS', 'age', 'shape', 'margin', 'density', 'severity'])
# print ('masses_data.head():')
# print (masses_data.head())

# Evaluate Data needs cleaning.
# print('Evaluate => masses_data.describe()')
# print(masses_data.describe())

# Print missing data row
# print ("misses_data.loc('age, shape, margin, density:')")
# print(masses_data.loc[(masses_data['age'].isnull()) |
#               (masses_data['shape'].isnull()) |
#               (masses_data['margin'].isnull()) |
#               (masses_data['density'].isnull())])

masses_data.dropna(inplace=True)
# print('dropna => masses_data.describe():')
# print(masses_data.describe())

# Convert dataframe into numpy array for scikit_learn
all_features = masses_data[['age', 'shape',
                             'margin', 'density']].values


all_classes = masses_data['severity'].values

feature_names = ['age', 'shape', 'margin', 'density']
# print ('masses_data.head():')
# print (masses_data.head())
# print('feature_names:')
# print(feature_names)
# print('panda df to numpy array => all_features[:5]:')
# print(all_features[:5])
# print('panda df to numpy array => all_classes[:5]:')
# print(all_classes[:5])

# Normalize Data. 
# Fit: Calculate mean (mu) and variance (sigma).
# Tarnsform into particlar train/test data set
from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
all_features_scaled = scaler.fit_transform(all_features)
# print ('Normalize, fit, transform => all_features_scaled[:5]:')
# print (all_features_scaled[:5])

import numpy
from sklearn.model_selection import train_test_split

numpy.random.seed(1234)

(training_inputs, testing_inputs, training_classes, testing_classes) = \
    train_test_split(all_features_scaled, all_classes, \
    train_size=0.75, random_state=1)
# print('Split data into training and test => training_inputs[:5]:')
# print(training_inputs[:5])
# print('training_classes[:5]:')
# print(training_classes[:5])

# o1: Decision Tree
from sklearn.tree import DecisionTreeClassifier
clf= DecisionTreeClassifier(random_state=1)
# Train the classifier on the training set
clf.fit(training_inputs, training_classes)
# Train the classifier on the training set
# print('clf:')
# print(clf)
# Display Decision Tree
# from IPython.display import Image  
import matplotlib.pyplot as plt
from sklearn.externals.six import StringIO  
from sklearn import tree
from pydotplus import graph_from_dot_data 
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=feature_names)  
graph = graph_from_dot_data(dot_data.getvalue())  
graph.write_pdf ("tree.pdf")
# Image(graph.create_png())
# Measure Accuracy
print ('01: Decision Tree => clf.score(testing_inputs, testing_classes):', \
    clf.score(testing_inputs, testing_classes))

# 02: Decision Tree: K-Fold Cross-Validation
from sklearn.model_selection import cross_val_score
clf = DecisionTreeClassifier(random_state=1)
cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
print ('02: Decision Tree: K-Fold Cross-Validation => cv_scores.mean():', cv_scores.mean())

# 03: SVM (Support Vector Machine)
from sklearn import svm
C = 1.0
svc = svm.SVC(kernel='linear', C=C)
cv_scores = cross_val_score(svc, all_features_scaled, all_classes, cv=10)
print('03: SVM => cv_scores.mean():', cv_scores.mean())

# 04: KNN (K-Nearest Neighbor)
from sklearn import neighbors
k = 10
clf = neighbors.KNeighborsClassifier(n_neighbors=k)
cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
print('04: KNN => ', 'k =', k, ', cv_scores.mean():', cv_scores.mean())

# for k in range(1, 20):
#     clf = neighbors.KNeighborsClassifier(n_neighbors=k)
#     cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
#     print ('k: ', k, 'cv_scores.mean():', cv_scores.mean())

# 05: Naive Bayes
from sklearn.naive_bayes import MultinomialNB
scaler = preprocessing.MinMaxScaler()
all_features_minmax = scaler.fit_transform(all_features)

clf = MultinomialNB()
cv_scores = cross_val_score(clf, all_features_minmax, all_classes, cv=10)
print('05: Naive Bayes => cv_scores.mean():', cv_scores.mean())

# 06: SVM-rbf
C = 1.0
svc = svm.SVC(kernel='rbf', C=C, gamma='auto')
cv_scores = cross_val_score(svc, all_features_scaled, all_classes, cv=10)
print('06: SVM-rbf => cv_scores.mean():', cv_scores.mean())

# 07: SVM-sigmoid
C = 1.0
svc = svm.SVC(kernel='sigmoid', C=C, gamma='auto')
cv_scores = cross_val_score(svc, all_features_scaled, all_classes, cv=10)
print('07: SVM-sigmoid => cv_scores.mean():', cv_scores.mean())

# 08: SVM-poly
C = 1.0
svc = svm.SVC(kernel='poly', C=C, gamma='auto')
cv_scores = cross_val_score(svc, all_features_scaled, all_classes, cv=10)
print('08: SVM-poly => cv_scores.mean():', cv_scores.mean())

# 09: Logistic Regression
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(solver='lbfgs')
cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
print('09: Logistic Regression => cv_scores.mean():', cv_scores.mean())

# 10: Neural Network
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

def create_model():
    model = Sequential()
    #4 feature inputs going into an 6-unit layer (more does not seem to help - in fact you can go down to 4)
    model.add(Dense(6, input_dim=4, kernel_initializer='normal', activation='relu'))
    # "Deep learning" turns out to be unnecessary - this additional hidden layer doesn't help either.
    #model.add(Dense(4, kernel_initializer='normal', activation='relu'))
    # Output layer with a binary classification (benign or malignant)
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    # Compile model; adam seemed to work best
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

# Wrap our Keras model in an estimator compatible with scikit_learn
estimator = KerasClassifier(build_fn=create_model, epochs=100, verbose=0)
# Now we can use scikit_learn's cross_val_score to evaluate this model identically to the others
cv_scores = cross_val_score(estimator, all_features_scaled, all_classes, cv=10)
print('10: Neural Network => cv_scores.mean():', cv_scores.mean())