import numpy as np
from scipy import stats

A = np.random.normal(25.0, 5.0, 100000)
B = np.random.normal(25.0, 5.0, 100000)
print('A[:5]):')
print(A[:5])
print('B[:5]):')
print(B[:5])
print('stats.ttest_ind(A, B):')
print(stats.ttest_ind(A, B))   
# Ttest_indResult(statistic=-0.2427170785149424, pvalue=0.8082248251703475)
# Low T-Value = -0.24, Very Low T-Value => two large exactly same test (Bad)
# Low P-Value = 0.80. High P-Value => Two test are consistent (This is Very Good)