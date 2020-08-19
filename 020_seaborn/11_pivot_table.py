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
df2=df.pivot_table(index='Cylinders', columns='Eng Displ', values='CombMPG', aggfunc='mean')
sns.heatmap(df2)

plt.show()
