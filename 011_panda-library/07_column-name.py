
import pandas as pd

df = pd.read_csv ('PastHires.csv')
print ('df.shape:', df.shape)
print ('df.columns:')
print (df.columns)  
# Index(['Years Experience', 'Employed?', 'Previous employers',
# 'Level of Education', 'Top-tier school', 'Interned', 'Hired'],
# dtype='object')
