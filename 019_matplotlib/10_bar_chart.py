import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Remove XKCD mode
plt.rcdefaults()
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0, 5), values, color=colors)
plt.title('Student Locations Percentage')
plt.show()
