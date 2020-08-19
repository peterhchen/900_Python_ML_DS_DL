import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#pd.read_csv('http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv')
df = pd.read_csv ('./FuelEfficiency.csv')
# Cylinders, CityMPG,HwyMPG,CombMPG
df2 = df [['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]

print('df2.head():')
print(df2.head())
# pair combined several together.
sns.pairplot(df2, hue='Cylinders', height=2.5)
plt.show()
