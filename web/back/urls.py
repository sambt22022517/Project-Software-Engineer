from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
   
    path('removepunc', views.removepunc, name='rempun'),
    path('capitalizefirst', views.capfirst, name='capfirst'),
    path('newlineremove', views.newlineremove, name='newlineremove'),
    path('spaceremove', views.spaceremove, name='spaceremove')
]