from django.urls import path
from .views import store_index, product_list

urlpatterns = [
    path('', store_index, name='index'),
    path('products/', product_list, name='list')
]
