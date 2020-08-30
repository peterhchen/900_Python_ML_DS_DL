# Read rating and movie
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', \
    sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', \
    sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)
print('ratings.head():')
print(ratings.head())

# construct user and movie rating matrix
import numpy as np
movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
na = np.array(movieRatings)
print('movieRatings.head():')
print(movieRatings.head())

# Extract Data
starWarsRatings = movieRatings['Star Wars (1977)']
print ('starWarsRatings.head():')
print (starWarsRatings.head())

# Correlate Data
similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
print ('df.head(10):')
print (df.head(10))