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