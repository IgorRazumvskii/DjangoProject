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

    path('response/<int:pk>', response, name='response'),
    path('responses/', ResponsesView.as_view(), name='responses'),

    path('response/delete/<int:pk>', ResponseDelete.as_view(), name='response_delete'),
    path('response/accept/<int:pk>', response_accept, name='response_accept'),

    path('response/update/<int:pk>', ResponseUpdate.as_view(), name='response_update')
]