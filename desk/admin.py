from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from .models import Product, Category, Response
# Register your models here.


class ProductAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Response)

