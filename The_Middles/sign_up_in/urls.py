from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.sign_up, name='sign-up'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('', views.home, name='home'),
]