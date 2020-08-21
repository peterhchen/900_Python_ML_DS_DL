import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

# df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
df = pd.read_excel('cars.xls')

scale = StandardScaler()

X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

print('X1.head():')
print(X.head())
print('y1.head():')
print(y.head())

X[['Mileage', 'Cylinder', 'Doors']] = \
    scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].values)

print('X.head():')
print(X.head())
print('y.head():')
print(y.head())

est = sm.OLS(y, X).fit()

est.summary()
print('est.summary():')
print(est.summary())