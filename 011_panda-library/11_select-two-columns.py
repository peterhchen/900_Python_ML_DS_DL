
import pandas as pd

df = pd.read_csv ('PastHires.csv')

print ('df.columns:')
print (df.columns)
# Select two columns.
print ("df[['Years Experience', 'Hired']]:")
print (df[['Years Experience', 'Hired']])
