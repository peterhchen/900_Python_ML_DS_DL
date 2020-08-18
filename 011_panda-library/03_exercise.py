import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ('PastHires.csv')

print ("df[['previous employers']['Hired]]:")
print (df[['Previous employers', 'Hired']])
hist = df[['Previous employers', 'Hired']][5:11]

print ('hist:', hist)
hist.plot(kind='bar')
plt.show()