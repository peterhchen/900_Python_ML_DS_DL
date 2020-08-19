import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#pd.read_csv('http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv')
df = pd.read_csv ('./FuelEfficiency.csv')
gear_counts = df['# Gears'].value_counts()
print ('gear_counts:')
print (gear_counts)
gear_counts.plot(kind='bar')
plt.show()
