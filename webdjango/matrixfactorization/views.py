from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import Http404
from shop.models import Product, Review
from django.contrib import messages

from django.db.models import Case, When
from .recommendation import Myrecommend
import numpy as np
import pandas as pd


# for recommendation
def recommend(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404
    df = pd.DataFrame(list(Review.objects.all().values()))
    nu = df.user_name.unique().shape[0]
    current_user_id = request.user_id
    # if new user not rated any movie
    if user_name > nu:
        product = Product.objects.get(id=15)
        q = Review(user=request.user, product=product, rating=0)
        q.save()

    print("Current user id: ", current_user_id)
    prediction_matrix, Ymean = Myrecommend()
    my_predictions = prediction_matrix[:, current_user_id - 1] + Ymean.flatten()
    pred_idxs_sorted = np.argsort(my_predictions)
    pred_idxs_sorted[:] = pred_idxs_sorted[::-1]
    pred_idxs_sorted = pred_idxs_sorted + 1
    print(pred_idxs_sorted)
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pred_idxs_sorted)])
    movie_list = list(Product.objects.filter(id__in=pred_idxs_sorted, ).order_by(preserved)[:10])
    return render(request, 'web/recommend.html', {'movie_list': movie_list})

def recom(request, k=8):
    user_name = request.user.username
    all_users = User.objects.all()
    data_for_uuCF = []
    product_ids = []
    for product_id, name, rating in all_reviews:
        user_id = user_id_dict.get(name)
        data_for_uuCF.append([user_id, product_id, rating])  # Adjust column order if needed
        product_ids.append(product_id)  # Store product IDs for later use
    model = uuCF(data_for_uuCF, k=k)
    model.fit()

    predictions = {}
    for product_id in product_ids:
        predicted_rating = model.pred(user_id_dict.get(user_name), product_id)
        predictions[product_id] = predicted_rating

    # Filter out already rated products
    user_reviews = Review.objects.filter(user_name=user_name).values_list("product_id", flat=True)
    already_rated_product_ids = set(user_reviews)

    # Sort and select top-k recommendations
    recommendations = []
    for product_id, predicted_rating in predictions.items():
        if product_id not in already_rated_product_ids:
            recommendations.append((product_id, predicted_rating))
    recommendations.sort(key=lambda x: x[1], reverse=True)  # Sort by predicted rating
    top_k_recommendations = recommendations[:k]

    # Retrieve recommended products
    recommended_product_ids = [rec[0] for rec in top_k_recommendations]
    recommended_products = Product.objects.filter(id__in=recommended_product_ids)
    context = {
        "movie_list": recommended_products,
        "user_id": request.user.id,
    }
    return render(request, "recommend.html", context)
