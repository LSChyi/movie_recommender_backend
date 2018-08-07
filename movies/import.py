import pandas as pd
from movies.models import Movie, MovieTrailer

movies = pd.read_csv('movies/movies.csv')
for _, row in movies.iterrows():
    row_dict = row.to_dict()
    del row_dict['type']
    Movie.objects.create(**row_dict)

trailers = pd.read_csv('movies/trailers.csv')
for _, row in trailers.iterrows():
    row_dict = row.to_dict()
    MovieTrailer.objects.create(**row_dict)
