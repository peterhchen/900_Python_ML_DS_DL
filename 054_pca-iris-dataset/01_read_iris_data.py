# Read Iris Data
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

iris = load_iris()

numSamples, numFeatures = iris.data.shape
print('numSamples:', numSamples)
print('numFeatures:', numFeatures)
print('list(iris.target_names):')
print(list(iris.target_names))