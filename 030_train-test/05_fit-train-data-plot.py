import numpy as np
from pylab import *
import matplotlib.pyplot as plt

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

# scatter(pageSpeeds, purchaseAmount)
# plt.show()

trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

x = np.array(trainX)
y = np.array(trainY)
p8 = np.poly1d (np.polyfit(x, y, 8))

print('p8:')
print(p8)

xp = np.linspace (0, 7, 100)
axes = plt.axes ()
axes.set_xlim([0, 7])
axes.set_ylim ([0, 200])

scatter(x, y)
plt.plot(xp, p8(xp), c='r')
plt.show()