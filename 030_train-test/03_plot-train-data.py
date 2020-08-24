import numpy as np
from pylab import *
import matplotlib.pyplot as plt

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)
plt.show()

# (0-79)/100 = 80%
# (80-99)/100 = 20%
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

print('trainX[:5]:', trainX[:5])
print('testX[:5]:', testX[:5])
print('trainY[:5]:', trainY[:5])
print('testY[:5]:', testY[:5])

scatter(trainX, trainY)
plt.show()

scatter(testX, testY)
plt.show()