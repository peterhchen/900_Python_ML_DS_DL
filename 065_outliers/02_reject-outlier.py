
import matplotlib.pyplot as plt
import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
incomes = np.append(incomes, [1000000000])

# plt.hist(incomes, 50)
# plt.show()
# print ('incomes.mean():')
# print (incomes.mean())

# REject Outliers
def reject_outliers(data):
    u = np.median(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered

filtered = reject_outliers(incomes)

plt.hist(filtered, 50)
plt.show()

print ('incomes.mean():')
print (incomes.mean())
filterednp = np.asarray(filtered)
print ('\nfilterednp.mean():')
print (filterednp.mean())