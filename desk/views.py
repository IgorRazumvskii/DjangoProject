from django.shortcuts import render
from .models import *
from .forms import ProductForm

from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy


#  список объявлений
class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 50


#  просмотр объявления
class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


#  создание объявления
class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'


#  изменение объявления
class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'


#  удаление объявления
class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')
