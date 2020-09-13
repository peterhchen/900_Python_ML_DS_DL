import numpy as np
from scipy import stats

A = np.random.normal(25.0, 5.0, 10000)
B = np.random.normal(26.0, 5.0, 10000)
print('A[:5]):')
print(A[:5])
print('B[:5]):')
print(B[:5])
print('stats.ttest_ind(A, B):')
print(stats.ttest_ind(A, B))   
# Ttest_indResult(statistic=-15.123658741265006, pvalue=2.1763964882047815e-51)
# high T-Value = -15, data are two different test (Good)
# Low P-Value = 2.1^-15. (data are not consistent) High P-Value are consistent (Bad)