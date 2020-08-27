# Make data for people clustered by income and age randomly.

from numpy import random, array

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

#Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X = array(X)
    return X

# We'll use k-means to rediscover these clusters 
# in unsupervised learning.

data = createClusteredData(100, 5)

model = KMeans(n_clusters=5)
# Note I'm scaling the data to normalize it! Important for good results.
model = model.fit(scale(data))

# We can look at the clusters each data point was assigned to
print(model.labels_)

# And we'll visualize it:
plt.figure(figsize=(8, 6))
# plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.scatter(data[:,1], data[:,0], c=model.labels_.astype(float))
plt.show()
