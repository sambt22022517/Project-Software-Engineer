from django.urls import path
from . import views

urlpatterns = [
    path('thanh-toan/', views.test_thanh_toan, name='thanh-toan'),
]