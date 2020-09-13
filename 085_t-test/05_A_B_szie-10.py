import numpy as np
from scipy import stats

A = np.random.normal(25.0, 5.0, 10)
B = np.random.normal(25.0, 5.0, 10)
print('A[:5]):')
print(A[:5])
print('B[:5]):')
print(B[:5])
print('stats.ttest_ind(A, B):')
print(stats.ttest_ind(A, B))   
# Ttest_indResult(statistic=0.0, pvalue=1.0)
# Ttest_indResult(statistic=1.3155688693883234, pvalue=0.20483022418300662)