from pyspark.mllib.clustering import KMeans
from numpy import array, random
from math import sqrt
from pyspark import SparkConf, SparkContext
from sklearn.preprocessing import scale

K = 5

# Boilerplate Spark stuff:
conf = SparkConf().setMaster("local").setAppName("SparkKMeans")
sc = SparkContext(conf = conf)

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

random.seed(0)

# Load the data; note I am normalizing it with scale() - very important!
data = sc.parallelize(scale(createClusteredData(100, K)))
# data = sc.parallelize(createClusteredData(100, K))
# Build the model (cluster the data)
print ('maxiteraton = 10')
clusters = KMeans.train(data, K, maxIterations=10, initializationMode="random")
# Print out the cluster assignments
resultRDD = data.map(lambda point: clusters.predict(point)).cache()

# print("Counts by value:")
counts = resultRDD.countByValue()
# print('counts:')
# print(counts)

# print("Cluster assignments:")
results = resultRDD.collect()
# print('results:')
# print(results)

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    # print('point:', point)      # point (X, Y) = [ 0.2557521  -0.29963796]
    # print('center:', center)    # center (x, y) = center: [ 0.12375048 -0.27096109]
    # pc = (point - center)       
    # print ('pc: ', pc)          # pc:  [ 0.13200162 -0.02867688]
    # # for x in (point - center):
    # for x in pc:
    #     print ('x:', x)         # x: 0.1320016202053304, x: -0.02867687536948088
    # print ()
    return sqrt(sum([x**2 for x in (point - center)]))

# data.map(lambda point: error(point))                              # Does not print any point
# data.map(lambda point: error(point)).reduce(lambda x, y: x + y)   # print 100 point

WSSSE = data.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))

# Things to try:
# What happens to WSSSE as you increase or decrease K? Why?
# What happens if you don't normalize the input data before clustering?
# What happens if you change the maxIterations or runs parameters?
