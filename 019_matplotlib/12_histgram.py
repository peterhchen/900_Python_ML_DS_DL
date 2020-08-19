import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Remove XKCD mode
plt.rcdefaults()
# normal (array, scale/std, size)
incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50)
plt.title('Scatter Plot')
plt.show()
