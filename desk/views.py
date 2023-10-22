from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import mail_managers, send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from .models import *
from .filters import CustomFilter
from .forms import ProductForm, ResponseForm


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
class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

    #  добавление юзера
    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        return super().form_valid(form)


#  изменение объявления
class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')


#  удаление объявления
class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


#  личный кабинет
class CabinetView(LoginRequiredMixin, TemplateView):
    template_name = 'cabinet.html'


#  просмотр откликов
class ResponsesView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = CustomFilter(self.request.GET, queryset)
        self.filterset = CustomFilter(self.request.GET,
                                      queryset.filter(product__user=self.request.user, request=False))
        print(self.filterset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        #print(context)
        return context


#  удаление отклика
class ResponseDelete(LoginRequiredMixin, DeleteView):
    model = Response
    template_name = 'response_delete.html'
    context_object_name = 'response'
    success_url = reverse_lazy('responses')


#  добавление текста отклика
class ResponseUpdate(LoginRequiredMixin, UpdateView):
    model = Response
    form_class = ResponseForm
    template_name = 'response_create.html'
    success_url = reverse_lazy('product_list')


#  принять запрос
@login_required
def response_accept(request, pk):
    response = Response.objects.filter(pk=pk).first()
    response.request = True
    response.save()
    send_mail(
        f'{response.user}',
        f'Ваш запрос принят',
        'razumovskijigor6@gmail.com',
        [response.user.email],
        fail_silently=False,
    )
    return redirect('responses')


#  отправка отклика
@login_required
def response(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    r = Response.objects.create(product=product, user=user)
    return redirect(f'/response/update/{r.pk}')
