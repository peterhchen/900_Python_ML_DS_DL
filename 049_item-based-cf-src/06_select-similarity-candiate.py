# Read MovieLens 100K data
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', \
    names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', \
    names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)
print('ratings.head():')
print(ratings.head())

# Construct Matrix
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print('userRatings.head():')
print(userRatings.head())

# correlation score
corrMatrix = userRatings.corr()
print('corrMatrix.head():')
print(corrMatrix.head())

# min threshold
corrMatrix = userRatings.corr(method='pearson', min_periods=100)
print('min threshold => corrMatrix.head():')
print(corrMatrix.head())

# Remove NA data
myRatings = userRatings.loc[0].dropna()
print('drop NA => myRatings:')
print(myRatings)

# Select Similarity Candidate
simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print ('Select Similarity Candidate => simCandidates.head(10):')
print (simCandidates.head(10))