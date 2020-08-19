import numpy as np
import matplotlib.pyplot as plt

# Normal distribution between 0 with std/scale = 0.5
# data point 10000
values = np.random.normal (0, 0.5, 10000)

plt.hist(values, 50)
plt.show()

# find the percentitle of 50, 90, and 20.
print ('np.percentile(values, 50): ', np.percentile (values, 50))
print ('np.percentile(values, 90): ', np.percentile (values, 90))
print ('np.percentile(values, 20): ', np.percentile (values, 20))