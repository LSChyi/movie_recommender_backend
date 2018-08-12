from celery import Celery

app = Celery('recommender.trainer', broker='redis://localhost', backend='redis://localhost')
app.conf.update(worker_concurrency=1, task_default_queue='trainer', accept_content=['pickle', 'json'], result_serializer='pickle')

@app.task
def train(queue):
    global ratings_df
    ratings_df = ratings_df.append(pd.DataFrame(queue, columns=['user_id', 'movie_id', 'rating', 'timestamp']))
    ratings = coo_matrix((ratings_df['rating'], (ratings_df['movie_id'], ratings_df['user_id'])))
    model.fit(40 * ratings)
    return (model.user_factors, model.item_factors)

if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    from scipy.sparse import coo_matrix
    from implicit.als import AlternatingLeastSquares

    user_offset = 69878
    ratings_df = pd.read_csv('recommender/ratings.csv')
    ratings = coo_matrix((ratings_df['rating'], (ratings_df['movie_id'], ratings_df['user_id'])))
    model = AlternatingLeastSquares(factors=32, regularization=0.01, dtype=np.float32, iterations=15, calculate_training_loss=True)
    app.worker_main()
