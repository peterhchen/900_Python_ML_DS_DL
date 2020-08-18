import numpy as np
from scipy.stats import norm, binom
import matplotlib.pyplot as plt

# Generate PMF (Probability Mass Function) with Binom
# n: number of point, p: shape paremeter
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
# generate a discret PMF (Probability Mass function)
plt.plot (x, norm.pdf(x))
plt.show()
plt.plot (x, binom.pmf(x, n, p))
plt.show()
