import pandas as pd
import pandas as pd
from sklearn import tree

# Read Data
input_file = "PastHires.csv"
df = pd.read_csv(input_file, header = 0)
print ('df.ead():')
print (df.head())

# Translate:
# 1) text (Y, N) into values (1, 0)
# 2) text (BS, MS, PhD) into values (0, 1, 2)
d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
print ('map df.head():')
print (df.head())

# Get features
features = list(df.columns[:6])
print('features:')
print(features)

# Construct Decision Tree
y = df["Hired"]
X = df[features]
print('y[:5]:')
print(y[:5])
print('X[:5]:')
print(X[:5])

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, y)

#Predict employment of an employed 10-year veteran
print('clf.predict([[10, 1, 4, 0, 0, 0]]):')
print(clf.predict([[10, 1, 4, 0, 0, 0]]))
#...and an unemployed 10-year veteran
print ('clf.predict([[10, 0, 4, 0, 0, 0]]):')
print (clf.predict([[10, 0, 4, 0, 0, 0]]))