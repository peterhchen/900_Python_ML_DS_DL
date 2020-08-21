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

X[['Mileage', 'Cylinder', 'Doors']] = \
    scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].values)
est = sm.OLS(y, X).fit()

est.summary()
print('est.summary():')
print(est.summary())
# y.groupby(df.Doors).mean()
# print('y.groupby(df.Doors).mean():')
# print(y.groupby(df.Doors).mean())

# Make car price prediction
# Mileage = 45000, Cylinder = 8, Doors =4 
scaled = scale.transform([[45000, 8, 4]])
print('scaled:', scaled)
predicted = est.predict(scaled[0])
print('price predicted: ', predicted)