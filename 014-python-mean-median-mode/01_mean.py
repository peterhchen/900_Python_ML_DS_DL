import numpy as np
import matplotlib.pyplot as plt

# Generate income data: 
# Centered around 27,000. 
# Standard deviation 15,000
# Data point: 10,000
incomes = np.random.normal(27000, 15000, 10000)
print('np.mean(incomes):', np.mean(incomes))

# Plot the incomes data into 50 bins (buckets)
plt.hist (incomes, 50)
plt.show()