from datetime import timedelta
from celery import Celery
from celery.task import periodic_task
from celery.result import allow_join_result
from .trainer import train

app = Celery('recommender.dispatcher', broker='redis://localhost', backend='redis://localhost')
app.conf.update(worker_concurrency=1, task_default_queue='dispatcher')

@app.task
def recommend(user_id):
    global user_items, model
    l = model.recommend(userid=user_id, user_items=user_items, N=30)
    return list(map(lambda id: int(id[0]) , l))

@app.task
def add_rating(user_id, movie_id, rating):
    global ratings_df, queue, ratings, user_items
    ratings_df = ratings_df.append(
        pd.DataFrame([{
            'user_id': user_id,
            'movie_id': movie_id,
            'rating': rating,
            'timestamp': None
        }]),
        ignore_index=True
    )
    queue.append([ user_id, movie_id, rating, None ])
    ratings = coo_matrix((ratings_df['rating'], (ratings_df['movie_id'], ratings_df['user_id'])))
    user_items = ratings.T.tocsr()

@periodic_task(run_every=timedelta(seconds=3))
def run_runtine():
    global ratings_df, queue, train_task, model
    if not train_task or train_task.ready():
        if train_task and train_task.ready():
            with allow_join_result():
                user_factors, item_factors = train_task.get()
                model.user_factors = user_factors
                model.item_factors = item_factors
                train_task = None

        if queue:
            train_task = train.apply_async((queue,), queue='trainer')
            # TODO save queue
            queue = []

if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    from scipy.sparse import coo_matrix
    from implicit.als import AlternatingLeastSquares

    user_offset = 69878
    ratings_df = pd.read_csv('recommender/ratings.csv')
    ratings = coo_matrix((ratings_df['rating'], (ratings_df['movie_id'], ratings_df['user_id'])))
    model = AlternatingLeastSquares(factors=32, regularization=0.01, dtype=np.float32, iterations=15, calculate_training_loss=True)
    model.user_factors = np.load('recommender/user_factors.npy')
    model.item_factors = np.load('recommender/item_factors.npy')
    user_items = ratings.T.tocsr()
    queue = []
    train_task = None
    app.worker_main()
