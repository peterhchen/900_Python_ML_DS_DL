import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(15,5)})

#pd.read_csv('http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv')
df = pd.read_csv ('./FuelEfficiency.csv')

#Mfr Name,Carline,Eng Displ,Cylinders, ..., CombMPG,# Gears
print('df.head():')
print(df.head())
# Slope and scatter plot

ax=sns.swarmplot(x='Mfr Name', y='CombMPG', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.show()
