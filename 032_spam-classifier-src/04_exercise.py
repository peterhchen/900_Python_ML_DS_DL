import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrameFromDirectory('emails/spam', 'spam'))
data = data.append(dataFrameFromDirectory('emails/ham', 'ham'))

# print('data.head(20): ')
# print(data.head(20))

# Split messsage into word tokens
# Vectorization (transform words into vector) and 
# Model the vector into linear regression 
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)
# print ('counts:')
# print (counts)
#print(counts.toarray())

classifier = MultinomialNB()
targets = data['class'].values
# print('targets[:10]: ')
# print(targets[:10])
classifier.fit(counts, targets)

# Message classifier
example1 = ['promotion', "coffee"]
example_counts = vectorizer.transform(example1)
prediction1 = classifier.predict(example_counts)
print ('example1 :', example1)
print ('prediction1:', prediction1)

example2 = ['accept credit', "tea"]
example_counts = vectorizer.transform(example2)
prediction2 = classifier.predict(example_counts)
print ('example2:', example2)
print ('prediction2:', prediction2)

example3= ['$$$$ affordable', "food"]
example_counts = vectorizer.transform(example3)
prediction3 = classifier.predict(example_counts)
print ('example3:', example3)
print ('prediction3:', prediction3)

example4= ['Make $', "cherry"]
example_counts = vectorizer.transform(example4)
prediction4 = classifier.predict(example_counts)
print ('example4:', example4)
print ('prediction4:', prediction4)

example5= ['Be Your Boss', "peach"]
example_counts = vectorizer.transform(example5)
prediction5 = classifier.predict(example_counts)
print ('example5:', example5)
print ('prediction5:', prediction5)
