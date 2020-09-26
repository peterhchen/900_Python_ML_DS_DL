
import pandas as pd

df = pd.read_csv ('PastHires.csv')
print ("df.columns:")
print (df.columns)
print ("df['Hired'][:5]:")
print (df['Hired'][:5])