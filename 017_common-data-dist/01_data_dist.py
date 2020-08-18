import numpy as np
import matplotlib.pyplot as plt

# Uniform distribution between -10 and 10 with data point 10000
values = np.random.uniform (-10, 10, 10000)

plt.hist(values, 50)
plt.show()
