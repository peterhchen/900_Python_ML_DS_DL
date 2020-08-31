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
