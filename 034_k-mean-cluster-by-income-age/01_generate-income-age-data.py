# Make data for people clustered by income and age randomly.

from numpy import random, array
import matplotlib.pyplot as plt

#Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    print ('N:', N)
    print ('k:', k)
    print ('pointsPerCluster: ', pointsPerCluster)
    X = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        print ('i:', i)
        print ('incomeCentroid:', incomeCentroid)
        ageCentroid = random.uniform(20.0, 70.0)
        print ('ageCentroid:', ageCentroid)
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X = array(X)
    return X

# We'll use k-means to rediscover these clusters 
# in unsupervised learning.

data = createClusteredData(100, 5)
x = []
y = []
for e in data:
    x.append(e[1])
    y.append(e[0])
print ('x[:5]:')
print (x[:5])
print ('y[:5:')
print (y[:5])
plt.scatter (x, y)
plt.show()