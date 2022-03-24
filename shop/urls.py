from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('cart/', views.shop, name='cart'),
    path('checkout/', views.shop, name='checkout'),
]
