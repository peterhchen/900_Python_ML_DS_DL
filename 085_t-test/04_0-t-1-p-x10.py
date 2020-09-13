import numpy as np
from scipy import stats

A = np.random.normal(25.0, 5.0, 100000)

print('A[:5]):')
print(A[:5])
print('stats.ttest_ind(A, A):')
print(stats.ttest_ind(A, A))   
# Ttest_indResult(statistic=0.0, pvalue=1.0)
# T-Value = 0, T-Value=0 => two exactly same test
# P-Value = 1.0. High P-Value => Two test are consistent (Very Good)