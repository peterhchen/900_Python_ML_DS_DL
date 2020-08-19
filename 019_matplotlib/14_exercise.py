import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Remove XKCD mode
plt.rcdefaults()
# low, high, size
ages = np.random.randint(1,  6, 100)
#print ('ages:', ages)
time = np.random.randint (1, 300, 100)
#print ('time:', time)
plt.scatter(ages, time)
plt.title('Scatter Plot of ages and times')
plt.xlabel ('age (year)')
plt.ylabel ('time (min)')
plt.show()
