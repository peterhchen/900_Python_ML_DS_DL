import numpy as np
import matplotlib.pyplot as plt

# centered at mu = 5 and deviation = 2.0 data point 10,000
mu = 5.0
sigma = 2.0
values = np.random.normal (mu, sigma, 10000) 

plt.hist (values, 50)
plt.show()
