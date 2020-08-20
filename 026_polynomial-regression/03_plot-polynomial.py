from pylab import *
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)
plt.show()

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4))

print('p4:')
print(p4)
xp = np.linspace(0, 7, 100)
print('xp[:5]:', xp[:5])
plt.scatter(x, y)
print('x[:5]:', x[:5])
print('y[:5]:', y[:5])
plt.plot(xp, p4(xp), c='r')
plt.show()
