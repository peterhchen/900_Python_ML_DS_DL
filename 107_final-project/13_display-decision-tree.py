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