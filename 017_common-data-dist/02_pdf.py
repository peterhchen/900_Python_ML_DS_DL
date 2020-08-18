import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# -3 to 3 with increment 0.001. 
# arrange (start, stop, step): return spaced value with given interval
# [-3., -2.999, -2.998, ...]
x = np.arange (-3, 3, 0.001)
# generate a continuous PDF (probability density function)
plt.plot (x, norm.pdf(x))
plt.show()
