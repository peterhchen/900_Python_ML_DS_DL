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
print ('masses_data.head():')
print (masses_data.head())
print('feature_names:')
print(feature_names)
print('panda df to numpy array => all_features[:5]:')
print(all_features[:5])
print('panda df to numpy array => all_classes[:5]:')
print(all_classes[:5])