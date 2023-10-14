from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDelete.as_view(), name='product_delete'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]