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

# Use PCA to reduce to two components
X = iris.data
pca = PCA(n_components=1, whiten=True).fit(X)
X_pca = pca.transform(X)
print('X_pca[:5]:')
print(X_pca[:5])
# PCA components
print('pca.components_:')
print(pca.components_)
# Additional PCA preserved information: PCA Variance Ratio
print('pca.explained_variance_ratio_:')
print(pca.explained_variance_ratio_)
print('sum(pca.explained_variance_ratio_):')
print(sum(pca.explained_variance_ratio_))