import pandas as pd
import pandas as pd
from sklearn import tree

# Read Data
input_file = "Exercise.csv"
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
clf = tree.DecisionTreeClassifier()
# Train model
clf = clf.fit(X,y)

print('y[:5]:')
print(y[:5])
print('X[:5]:')
print(X[:5])

# Create the graph tree from clf (classifier result)
# https://chrisalbon.com/machine_learning/trees_and_forests/visualize_a_decision_tree/
from IPython.display import Image  
from sklearn.externals.six import StringIO  
import pydotplus
import matplotlib.pyplot as plt

dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=features)
# draw graph  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) 
print ('graph:')
print(graph) 
# show graph: This does not show
Image(graph.create_png()) 
# Create PDF
graph.write_pdf("07_exercise_decision_tree.pdf")
# Create PNG
graph.write_png("07_exercise_decision_tree.png")
# plt.show()