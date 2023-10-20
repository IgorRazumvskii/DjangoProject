from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDelete.as_view(), name='product_delete'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('cabinet/', CabinetView.as_view(), name='cabinet'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('responses/', ResponsesView.as_view(), name='responses')
]