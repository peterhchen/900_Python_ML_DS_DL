import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Remove XKCD mode
plt.rcdefaults()
# Generate 100 random number: 0 to 1 
# scale 100: 0 to 100
# Shift -40: -40 to 60
uniformedSkewed = (np.random.rand(100) * (100)) - 40
# Generate 10 randim number: 0 to 1
# scale 50: 0 to 50
# shift +100: 100 to 150 
high_outliers = (np.random.rand(10) * (50)) + 100
# Generate 10 randim number: 0 to 1
# scale -50: 0 to -50
# shift -100: -100 to -150 
low_outliers = (np.random.rand(10) * (-50)) - 100

data = np.concatenate ((uniformedSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.title('Box and WHisker Plot')
plt.show()
