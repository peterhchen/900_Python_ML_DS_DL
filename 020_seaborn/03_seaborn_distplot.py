import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#pd.read_csv('http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv')
df = pd.read_csv ('./FuelEfficiency.csv')
print('df.head():')
print(df.head())
# distplot is the hist of matplotlib.
# distrplot automatically decide the default number of bins.
sns.distplot(df['CombMPG'])
print("df['CombMPG']:")
print(df['CombMPG'])
plt.show()
