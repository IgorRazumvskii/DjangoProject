# Generated by Django 4.2.6 on 2023-10-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Танки', 'Танки'), ('Хилы', 'Хилы'), ('ДД', 'ДД'), ('Торговцы', 'Торговцы'), ('Гилдмастеры', 'Гилдмастеры'), ('Квистгиверы', 'Квистгиверы'), ('Кузнецы', 'Кузнецы'), ('Кожевники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастера заклинаний', 'Мастера заклинаний')], max_length=20),
        ),
    ]