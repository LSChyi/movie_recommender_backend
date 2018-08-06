# movie_recommender_backend
Backend of the movie recommender system

# Installation

First, install dependiencies: 

	pip install -r requirments.txt
	
 and config the local settings and secret settings. There are examples for each setting file. The example of local settings is locate at `/recommender_backend/local_settings.py.example`; the example of secret settings is locate at `/recommender_backend/secret_settings.py.example`.

Next, create database and create super user:
	
	python3 manage.py migrate
	python3 manage.py createsuperuser