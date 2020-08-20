import numpy as np
from scipy import stats
from pylab import *
import matplotlib.pyplot as plt

def predict(x):
    return slope * x + intercept

# pageSpeeds = np.random.normal (3.0, 1.0, 1000)
# purchaseAmount = 100 - (pageSpeeds + np.random.normal (0, 0.1, 1000)) * 3
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
# Increase the devivation in random variable and 
# see the effect of r-value
pageSpeeds1 = np.random.normal (3.0, 2.0, 1000)
purchaseAmount1 = 100 - (pageSpeeds1 + np.random.normal (0, 1.5, 1000)) * 3
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress (pageSpeeds1, purchaseAmount1)
print('slope1:', slope1)
print('intercept1:', intercept1)
print('r_value1:', r_value1)
print('p_value1:', p_value1)
print('std_err1:', std_err1)

fitLine1 = predict(pageSpeeds1)
print('fitLine1[:5]:')
print(fitLine1[:5])

plt.scatter(pageSpeeds1, purchaseAmount1)
plt.plot(pageSpeeds1, fitLine1, c='r')
plt.show()