# movie_recommender_backend
Backend of the movie recommender system

# Installation

First, install dependiencies: 

	pip install -r requirments.txt
	
 and config the local settings and secret settings. There are examples for each setting file. The example of local settings is locate at `/recommender_backend/local_settings.py.example`; the example of secret settings is locate at `/recommender_backend/secret_settings.py.example`.

Next, create database and create super user:
	
	python3 manage.py migrate
	python3 manage.py createsuperuser
	
## Import Movie Data
There is a script to import movie data into database. Place your `movies.csv` and `trailers.csv` in the movies module, and run

	python3 manage.py shell < movies/import.py

to import the movie data from Movielens.