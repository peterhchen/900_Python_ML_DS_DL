import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generate the normal distribution around 100 with deviation 20 for 10000
# plot into 50 bins
# Find the Mean and Median
incomes = np.random.normal (100, 20, 10000)

plt.hist(incomes, 50)
plt.show()

# Find std and variance
print ('np.std(incomes):', np.std(incomes))
print ('np.var(incomes):', np.var(incomes))