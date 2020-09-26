
import pandas as pd

df = pd.read_csv ('PastHires.csv')
print ('df.tail(4)', df.tail(4))
# df.tail(4)     Years Experience Employed?  Previous employers Level of Education Top-tier school Interned Hired
#9                  0         N                   0                 BS               N        N     N
#10                 1         N                   1                PhD               Y        N     N
#11                 4         Y                   1                 BS               N        Y     Y
#12                 0         N                   0                PhD               Y        N     Y