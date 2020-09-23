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
print('Evaluate => masses_data.describe()')
print(masses_data.describe())