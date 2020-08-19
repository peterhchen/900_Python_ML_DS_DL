import numpy as np
import matplotlib.pyplot as plt

def de_mean (x):
    xmean = np.mean (x)
    return [xi - xmean for xi in x]

def covariance (x, y):
    n = len (x)
    return np.dot (de_mean (x), de_mean(y))/(n-1)

pageSpeeds = np.random.normal (3.0, 1.0, 1000)
# purchaseAmount = np.random.normal (50.0, 10.0, 1000)
purchaseAmount = np.random.normal (50.0, 10.0, 1000) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)
print ('covariance (pageSpeeds, purchaseAmount): ', covariance (pageSpeeds, purchaseAmount))
plt.show()
