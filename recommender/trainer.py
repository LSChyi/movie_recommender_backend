from celery import Celery

app = Celery('recommender.trainer', broker='redis://localhost', backend='redis://localhost')
app.conf.update(worker_concurrency=1, task_default_queue='trainer')

@app.task()
def train():
    model.fit(40 * ratings)

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
    user_items = ratings.tocsr()
    app.worker_main()
