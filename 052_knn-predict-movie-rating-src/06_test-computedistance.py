# Read Movie Data
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', \
    names=r_cols, usecols=range(3))
print('ratings.head():')
print(ratings.head())

# Group by Movie ID
import numpy as np

movieProperties = \
    ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
print('movieProperties.head():')
print(movieProperties.head())

# Normalize Movie Rating
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = \
    movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
print('movieNormalizedNumRatings.head():')
print(movieNormalizedNumRatings.head())

# Read Genre Data
print ('Read Genre Data:')
movieDict = {}
with open(r'ml-100k/u.item') as f:
    temp = ''
    i = 0
    for line in f:
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres1 = fields[5:25]
        # convert character string into numpy integer array.
        genres = map(int, genres1)  
        if (i < 1):
            print ('fields:', fields)
            print ('movieID:', movieID)
            print ('name:', name)
            print ('genres1:', genres1)
            print ('genres:', genres)
        movieDict[movieID] = \
            (name, np.array(list(genres)), \
            movieNormalizedNumRatings.loc[movieID].get('size'), \
            movieProperties.loc[movieID].rating.get('mean'))
        if (movieID <= 5):
            print ('movieDict[', movieID,']:')
            print (movieDict[movieID])
        i += 1

# Compute Distance
from scipy import spatial
print ('\nCompute Distance:')
def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    # print('genresA:', genresA)
    # print('genresB:', genresB)
    # print('genreDistance:', genreDistance)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    # print('popularityA:', popularityA)
    # print('popularityB:', popularityB)
    # print('popularityDistance:', popularityDistance)
    return genreDistance + popularityDistance

# The higher the distance, the less similar
print('movieDict[2]:', movieDict[2])
print('movieDict[4]:', movieDict[4])
# Compoute Distance between ID = 2 and ID = 4.   
print('\nComputeDistance(movieDict[2], movieDict[4]):') 
print(ComputeDistance(movieDict[2], movieDict[4]))

# Compute Distance: Test Toy Story
import operator

def getNeighbors(movieID, K):
    print ('movie ID:', movieID)
    distances = []
    i = 0
    for movie in movieDict:
        if (i <= 5):
            print ('movie:', movie)
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
        i += 1

    #distances.sort(key=operator.itemgetter(1))
    print('distances.sort(key=operator.itemgetter(1)):')
    print(distances.sort(key=operator.itemgetter(1)))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    print ('neighbors:', neighbors)
    return neighbors

K = 10
avgRating = 0
print ('\nCompute Distance for Toy Story (ID = 1) with nearest 10 ratings:')
neighbors = getNeighbors(1, K)

for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))

# Compute average rate of 'Toy Story':
avgRating /= K
print('\n10 neighbors average around Toy Story (ID = 1):')
print('avgRating:', avgRating)

# Compare the average Rating (10 neighbors average) vs Toy Story (ID = 1)
print('Toy Story:')
# 'name: Toy Story', gnere array, normalize size, rating
print('movieDict[1]:')
print(movieDict[1])