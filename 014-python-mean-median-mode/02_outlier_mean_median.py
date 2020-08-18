import numpy as np
import matplotlib.pyplot as plt

# Generate income data: 
# Centered around 27,000. 
# Standard deviation 15,000
# Data point: 10,000
incomes = np.random.normal(27000, 15000, 10000)
print('np.mean(incomes):', np.mean(incomes))
print('np.median(incomes):', np.median(incomes))

# now, we add Jeff Bezos into unusual income
incomes = np.append(incomes, [1000000000])
print('outlier np.mean(incomes):', np.mean(incomes))
print('outlier np.median(incomes):', np.median(incomes))

# Plot the incomes data into 50 bins (buckets)
plt.hist (incomes, 50)
plt.show()