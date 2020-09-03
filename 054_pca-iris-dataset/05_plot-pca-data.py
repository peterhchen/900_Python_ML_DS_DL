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
pca = PCA(n_components=2, whiten=True).fit(X)
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

import matplotlib.pyplot as plt
from pylab import *

colors = cycle('rgb')   # 'rgb' => r g b
print ('\nPlot pca data:')
ic = 0
for color in colors:
    print (color)       # r g b
    ic += 1
    if ic >= 3:
        break
target_ids = range(len(iris.target_names))
print ('\ntarget_ids:', target_ids)   # range (0, 3)
print('\niris.target_names:', iris.target_names) 
# ['setosa' 'versicolor' 'virginica']
plt.figure()
print('\ni, c, label:') 
for i, c, label in zip(target_ids, colors, iris.target_names):
    print ('i:', i); print ('c:', c); print('label:', label)
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
        c=c, label=label)
print('\nX_pca[:5]:')
print(X_pca[:5])
plt.legend()
plt.show()
    