import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Remove XKCD mode
plt.rcdefaults()
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0.2, 0, 0, 0, 0]
labels = ['India', 'United States', 'Russia', 'China','Europe']
plt.pie(values, colors=colors, labels = labels, explode = explode)
plt.title('Student Locations Percentage')
plt.show()
