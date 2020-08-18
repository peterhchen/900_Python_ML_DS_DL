import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ('PastHires.csv')
print ('df.shape:', df.shape)
print ('df.size:', df.size)
print ('len(df):', len(df))
print ('df.columns:')
print (df.columns)
print ("df['Hired']:")
print (df['Hired'])
print ("df['Hired'][:5]:")
print (df['Hired'][:5])
print ("df['Hired'][5]:")
print (df['Hired'][5])
# You need to pass in array of column name instead of a single column.
print ("df[['Years Experience', 'Hired']]:")
print (df[['Years Experience', 'Hired']])

print ("df[['Years Experience', 'Hired']][:5]:")
print (df[['Years Experience', 'Hired']][:5])

print ("df.sort_values(['Years Experience'])[:5]:")
print (df.sort_values(['Years Experience'])[:5])

degree_counts = df['Level of Education'].value_counts()
print ('degree_counts:', degree_counts)
degree_counts.plot(kind='bar')
plt.show()