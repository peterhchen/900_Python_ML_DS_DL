
import pandas as pd

df = pd.read_csv ('PastHires.csv')

print ("df[['Years Experience', 'Hired']][:5]:")
print (df[['Years Experience', 'Hired']][:5])
