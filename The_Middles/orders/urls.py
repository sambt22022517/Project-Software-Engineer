from django.urls import path
from . import views

urlpatterns = [
    path('gio-hang-da-dang-nhap/', views.test, name='test'),
]