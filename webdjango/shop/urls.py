
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('about/', views.about, name="about"),
    path('', include('django.contrib.auth.urls')),
    #path('oauth/', include('social_django.urls', namespace="social")),
    path('product_list_category/', views.product_list_category, name="list"),
    path('', views.index, name="index"),
    path('product_list', views.index, name='product_list'),
    path('search/', views.search_list, name='query'),
    #path('trending/', views.search_list, name ='query'),
    path('<slug:category_slug>/', views.product_list_category, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cat/<slug:subcategory_slug>/', views.product_list_subcategory, name='product_list_by_subcategory'),
    
    path('reviewlist/', views.review_list, name='review_list'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    path('product/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('review/user/<str:username>/', views.user_review_list, name='user_review_list'),
    path('review/user/', views.user_review_list, name='user_review_list'),
    path('recommendation/', views.user_recommendation_list, name='user_recommendation_list'),
]



