from django import forms
from .models import Product, Response
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='users')
        basic_group.user_set.add(user)
        return user


class ProductForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = [
            'header',
            'text',
            'category'
        ]


class ResponseForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = [
            'text'
        ]


class ProductAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'