# movie_recommender_backend
Backend of the movie recommender system

# Installation

First, install dependiencies: 

	pip install -r requirments.txt

, this will install all the required dependencies. There is one package call [implicit](https://github.com/benfred/implicit) which support Nvidia CUDA, and if the pip installed version does not support GPU, consider remove it and reinstall it manually.
	
 and config the local settings and secret settings. There are examples for each setting file. The example of local settings is locate at `/recommender_backend/local_settings.py.example`; the example of secret settings is locate at `/recommender_backend/secret_settings.py.example`.

Next, create database and create super user:
	
	python3 manage.py migrate
	python3 manage.py createsuperuser
	
## Other dependencies
redis are requied to be installed. For Nvidia CUDA, it is requied the version should be greater then 8.0 in order to use implicit with GPU support. It is highly recommended to use CUDA to speedup implicit, for the training process can be 50 times faster for running on a Nvidia 1080 Ti compares to run on a 4th gen i5 CPU. With the Nvidia 1080 Ti, the training time is less then 3s.
	
## Import Movie Data
There is a script to import movie data into database. Place your `movies.csv` and `trailers.csv` in the movies module, and run

	python3 manage.py shell < movies/import.py

to import the movie data from Movielens.

There are prepared `movies.csv` and `trailers.csv` on [Google drive](https://drive.google.com/drive/folders/1R_pKTIhejiKSQNf44oGTwmAQwC8oi1iu). Note: the movie id is rearranged with starting id 0, and all ids are consecutive. The movies are from the 10M dataset.

## Place Model and Rating File
The recommender is stored in the `recommender` forlder, which will run a trainer and a dispatcher when runner the website. These two module requied some files placed in `recommender` folder, which are:

1. `ratings.csv`: used to construct a sparse matrix
2. `user_factors.npy`: stores user factors
3. `item_factors.npy`: stores movie factors

, and after running, these files are automatically updated when receiving new ratings and when new model is trained.

There are prepared `ratings.csv`, `user_factors.npy` and `item_factors.npy` on [Google drive](https://drive.google.com/drive/folders/12S23JHsicDod5VQ4kIDeOfhZs1MQYSTP). Note: the user id and movie id are rearranged. Movie id is the same as the prepared `movies.csv` and `trailers.csv` on above. User id is rearranged with starting id 0, and all ids are consective. The ratings are from the 10M dataset.

# Running
To run this project, there are at leat three processes are running. One is to server the django, one is the trainer to train model, and one is a model cache and ratings cache between django and the trainer. These processes are communicated through redis.

As a result, the first step is to start redis server. After that, run the trainer process with the command

	python3 recommender/trainer.py

at the root of the project. Also, start the dispatcher by

	python3 -m recommender.dispatcher --beat

at the root of the project. At last, starts the django server with

	python3 manage.py runserver

to run a development server.