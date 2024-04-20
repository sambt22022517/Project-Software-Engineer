from django.urls import path
from . import views

urlpatterns = [
    path('gio-hang-da-dang-nhap/', views.test, name='test'),
    path('gio-hang-trong/', views.test_gio_hang_trong, name='test_gio_hang_trong'),
    path('gio-hang-chua-dang-nhap/', views.test_gio_hang_chua_dang_nhap, name='test_gio_hang_chua_dang_nhap')
]