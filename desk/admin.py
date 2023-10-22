from django import forms
from .forms import ProductAdminForm
from django.contrib import admin
from .models import Product, Category, Response, News
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Response)
admin.site.register(News)

