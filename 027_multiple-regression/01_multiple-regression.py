import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
df = pd.read_excel('cars.xls')

df1=df[['Mileage','Price']]
print('df1.head():')
print(df1.head())
bins =  np.arange(0,50000,10000)
print('bins:')
print(bins)
print("pd.cut(df1['Mileage'],bins).head():")
print(pd.cut(df1['Mileage'],bins).head())
groups = df1.groupby(pd.cut(df1['Mileage'],bins)).mean()
# mileage and price are mean of each milage group 
# (0-10000], (10000, 20000], (20000, 30000], ...
#                      Mileage         Price
#Mileage
# (0, 10000]       5588.629630  24096.714451
# (10000, 20000]  15898.496183  21955.979607
print('groups:')
print(groups)
groups['Price'].plot.line()
plt.show()