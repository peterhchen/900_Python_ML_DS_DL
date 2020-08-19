import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Remove XKCD mode
plt.rcdefaults()
X = np.random.randn(500)
Y = np.random.randn (500)
plt.scatter(X, Y)
plt.title('Scatter Plot')
plt.show()
