import numpy as np
from pylab import *
import matplotlib.pyplot as plt

pageSpeeds = np.random.normal (3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal (0, 0.1, 1000)) * 3

scatter (pageSpeeds, purchaseAmount)
plt.show()