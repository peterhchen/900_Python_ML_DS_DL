
import matplotlib.pyplot as plt
import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
outliers = np.random.normal(1000000000, 10, 5)
incomes = np.append(incomes, outliers)

# plt.hist(incomes, 50)
# plt.show()
# print ('incomes.mean():')
# print (incomes.mean())

# REject Outliers
def reject_outliers(data, n):
    u = np.median(data)
    s = np.std(data)
    filtered = [e for e in data if (u - n * s < e < u + n * s)]
    return filtered

filtered = reject_outliers(incomes, 5)

plt.hist(filtered, 50)
plt.show()

print ('incomes.mean():')
print (incomes.mean())
filterednp = np.asarray(filtered)
print ('\nfilterednp.mean():')
print (filterednp.mean())