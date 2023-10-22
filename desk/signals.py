from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import mail_managers, send_mail
from .models import Response, News
from django.contrib.auth.models import User


@receiver(post_save, sender=Response)
def response_signal(sender, instance, created, **kwargs):
    if created:
        product = instance.product.header
        user = instance.user.username
        user_mail = instance.user.email
        creater = instance.product.user.email

        send_mail(
            f'{user}',
            f'Вы отправили запрос на объявление {product}',
            'razumovskijigor6@gmail.com',
            [user_mail],
            fail_silently=False,
        )

        send_mail(
            f'Запрос на объявление',
            f'{user} оставил запрос на объявление {product}',
            'razumovskijigor6@gmail.com',
           [creater],
            fail_silently=False,
        )


@receiver(post_save, sender=News)
def news_signal(sender, instance, created, **kwargs):
    if created:
        header = instance.header
        text = instance.text
        users = User.objects.all()
        for user in users:
            send_mail(
                f'{header}',
                f'{text}',
                'razumovskijigor6@gmail.com',
                [user.email],
                fail_silently=False,
            )


@receiver(pre_save, sender=Response)
def response_accept(sender, instance, **kwargs):
    if instance.request == True:
        product = instance.product.header
        user = instance.user.username
        user_mail = instance.user.email

        send_mail(
            f'{user}',
            f'Принят запрос на  {product}',
            'razumovskijigor6@gmail.com',
            [user_mail],
            fail_silently=False,
            )