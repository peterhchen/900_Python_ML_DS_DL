import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#pd.read_csv('http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv')
df = pd.read_csv ('./FuelEfficiency.csv')

#Mfr Name,Carline,Eng Displ,Cylinders, ..., CombMPG,# Gears
print('df.head():')
print(df.head())
# scatter plot
sns.scatterplot(x='Eng Displ', y = "CombMPG", data = df)
plt.show()
