from django.urls import path
from . import views

app_name = 'commingsoon'

urlpatterns = [
    path('commingsoon/', views.test_commingsoon, name='test_commingsoon'),
]