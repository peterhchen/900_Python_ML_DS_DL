import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


plt.xkcd()
fig = plt.figure()
ax = fig.add_subplot (1, 1, 1)
ax.spines ['right'].set_color('none')
ax.spines ['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim ([-30, 10])
data = np.ones (100)
print ('data1:')
print(data)
data[70:] -= np.arange(30)
print ('np.arange(30):')
print (np.arange(30))
print ('data2:')
print (data)
plt.annotate (
    'Time Day:',
    xy=(70,1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))
    
plt.plot(data)

plt.xlabel ('time')
plt.ylabel ('health score')

plt.show()
