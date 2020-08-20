import numpy as np
from numpy import random
import matplotlib.pyplot as plt

random.seed(0)
totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0

for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = float(ageDecade)/100.0
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1

print ('totals:', totals)
print ('purchases:', purchases)
print ('totalPurchases:', totalPurchases)
# pageSpeeds = np.random.normal (3.0, 1.0, 1000)
# purchaseAmount = np.random.normal (50.0, 10.0, 1000)

# plt.scatter(pageSpeeds, purchaseAmount)
# print ('covariance (pageSpeeds, purchaseAmount): ', covariance (pageSpeeds, purchaseAmount))
# plt.show()
