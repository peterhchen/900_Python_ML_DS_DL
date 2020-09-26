import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Normal distribution between 0 with std/scale = 0.5
# data point 10000
values = np.random.normal (0, 0.5, 10000)

plt.hist(values, 50)
plt.show()

# Find the moments (first, second, third, fourth)
print ('First Moment => np.mean(values): ', np.mean (values))
print ('Second Moment => np.var(values): ', np.var (values))
print ('Third Moment => stats.skew(values): ', stats.skew (values))
print ('Fourth Moment => stats.kurtosis(values): ', stats.kurtosis (values))