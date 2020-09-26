import pandas as pd

df = pd.read_csv ('PastHires.csv')
# head(): display 5 rows
print('df.head():', df.head())
print()
# head(10): display 10 rows
print('df.head(10):', df.head(10))