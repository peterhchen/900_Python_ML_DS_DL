import numpy as np
from scipy import stats
from pylab import *
import matplotlib.pyplot as plt

def predict(x):
    return slope * x + intercept

pageSpeeds = np.random.normal (3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal (0, 0.1, 1000)) * 3

slope, intercept, r_value, p_value, std_err = stats.linregress (pageSpeeds, purchaseAmount)
print('slope:', slope)
print('intercept:', intercept)
print('r_value:', r_value)
print('p_value:', p_value)
print('std_err:', std_err)

fitLine = predict(pageSpeeds)
print('fitLine[:5]:')
print(fitLine[:5])

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()