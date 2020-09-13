import numpy as np
from scipy import stats

A = np.random.normal(25.0, 5.0, 10000)
B = np.random.normal(25.0, 5.0, 10000)
print('A[:5]):')
print(A[:5])
print('B[:5]):')
print(B[:5])
print('stats.ttest_ind(A, B):')
print(stats.ttest_ind(A, B))   
# Ttest_indResult(statistic=0.664499204883276, pvalue=0.5063785195066963)
# Low T-Value = 0.66, Low T-Value => two same test (Bad)
# Low P-Value = 0.50. High P-Value => Two test are consistent (Good)