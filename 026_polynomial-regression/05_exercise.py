from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

# scatter(pageSpeeds, purchaseAmount)
# plt.show()

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4))
p10 = np.poly1d(np.polyfit(x, y, 10))
print('p4:')
print(p4)
print('p10:')
print(p10)
xp = np.linspace(0, 7, 100)
print('xp[:5]:', xp[:5])
plt.scatter(x, y)
print('x[:5]:', x[:5])
print('y[:5]:', y[:5])
plt.plot(xp, p4(xp), c='r')
plt.plot(xp, p10(xp), c='g')
plt.show()

r4 = r2_score(y, p4(x))
r10 = r2_score(y, p10(x))
print('r4:', r4)
print('r10:', r10)