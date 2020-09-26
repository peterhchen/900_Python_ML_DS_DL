
import pandas as pd

df = pd.read_csv ('PastHires.csv')

print ('df.columns:')
print (df.columns)

print ("df.sort_values(['Years Experience']):")
print (df.sort_values(['Years Experience']))
