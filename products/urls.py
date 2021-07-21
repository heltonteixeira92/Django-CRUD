from django.urls import path
from .views import list_products, create_product

urlpatterns = [
    path('', list_products, name='list_products'),
    path('new', create_product, name='create_product'),
]