
import pandas as pd


input_file = "PastHires.csv"
df = pd.read_csv(input_file, header = 0)
print ('df.head():')
print (df.head())