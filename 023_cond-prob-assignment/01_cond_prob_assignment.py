from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0
# First we'll modify the code to have some fixed purchase probability 
# regardless of age, say 40%:
for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    # purchaseProbability = float(ageDecade)/100.0
    purchaseProbability = 0.4
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1

# Next we will compute P(E|F) for some age group, 
# let's pick 30 year olds again:
PEF = float(purchases[30]) / float(totals[30])
print("P(purchase | 30s): ", PEF)

# Now we'll compute P(E)
PE = float(totalPurchases) / 100000.0
print("P(Purchase):", PE)
# P(E|F) is pretty close to P(E), so we can say that E and F are
# likely independent variables.
