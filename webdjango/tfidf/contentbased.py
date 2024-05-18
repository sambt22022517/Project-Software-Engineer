
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from shop.models import Product

def getFrames():
    # ds = Product.objects.all()

    # tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 5),
    #                      min_df=0, stop_words='english')
    # tfidf_matrix = tf.fit_transform([product.name for product in ds])

    # cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    results = {}

    # for idx, product in enumerate(ds):
    #     similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    #     similar_items = [(cosine_similarities[idx][i], ds[i].id)
    #                      for i in similar_indices]

    #     results[product.id] = similar_items[1:]
    # return results

def recommend(item_id, num, results):
    ids = []
    recs = results[item_id][:num]
    for rec in recs:
        ids.append(rec[1])
    return Product.objects.filter(id__in=ids)

results = getFrames()
