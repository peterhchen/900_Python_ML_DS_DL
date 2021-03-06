import numpy as np
from pylab import *
import matplotlib.pyplot as plt

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)
plt.show()

trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

scatter(trainX, trainY)
plt.show()

scatter(testX, testY)
plt.show()

x = np.array(trainX)
y = np.array(trainY)
p8 = np.poly1d (np.polyfit(x, y, 8))

print('p8:')
print(p8)