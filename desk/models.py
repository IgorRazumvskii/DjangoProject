from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

CHOICES = [
    ('Танки', 'Танки'),
    ('Хилы', 'Хилы'),
    ('ДД', 'ДД'),
    ('Торговцы', 'Торговцы'),
    ('Гилдмастеры', 'Гилдмастеры'),
    ('Квистгиверы', 'Квистгиверы'),
    ('Кузнецы', 'Кузнецы'),
    ('Кожевники', 'Кожевники'),
    ('Зельевары', 'Зельевары'),
    ('Мастера заклинаний', 'Мастера заклинаний'),
]


class Category(models.Model):
    name = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.name


class Product(models.Model):
    header = models.CharField(max_length=20)
    text = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        pass

    def get_absolute_url(self):
        return reverse('product_list')  # ???


class Response(models.Model):
    request = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='responses')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
