import numpy as np
from scipy.stats import expon, norm
import matplotlib.pyplot as plt

# 0 to 10 with increment 0.001. 
# arrange (start, stop, step): return spaced value with given interval
# [0., 0.001, -2.998, ...]
x = np.arange (-3, 3, 0.001)
# generate a continuous PDF (probability density function)
plt.plot (x, norm.pdf(x))
plt.show()
plt.plot (x, expon.pdf(x))
plt.show()
