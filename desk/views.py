from django.shortcuts import render
from .models import *
from .forms import ProductForm

from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.urls import reverse_lazy


#  список объявлений
class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 50


#  просмотр объявления
class ProductDetail(DetailView):
    form_class = ProductForm
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


class CabinetView(TemplateView):
    template_name = 'cabinet.html'


class ResponsesView(ListView):
    model = Product
    template_name = 'responses.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter()


