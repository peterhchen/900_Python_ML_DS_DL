import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

values = np.arange (-3, 3, 0.001)

plt.plot(values, norm.pdf(values))
plt.show()
