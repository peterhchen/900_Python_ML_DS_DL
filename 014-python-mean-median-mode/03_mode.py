import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generate the age between 18 to 90 with 500 people
ages = np.random.randint (18, high=90, size=500)
print ('ages:', ages)
print ('stats.mode(ages):')
print (stats.mode(ages))
# Plot the ages data into 500 bins (buckets)
plt.hist (ages, 500)
plt.show()