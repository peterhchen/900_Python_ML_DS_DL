
import pandas as pd
df = pd.read_csv('PastHires.csv')
degree_counts = df['Level of Education'].value_counts()
print('degree_counts:')
print(degree_counts)
