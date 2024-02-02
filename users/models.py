import random

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

code = ''.join([str(random.randint(0, 9)) for _ in range(12)])


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)

    avatar = models.ImageField(verbose_name='аватар', upload_to='users/', **NULLABLE)
    phone_number = models.CharField(max_length=40, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    ver_code = models.CharField(max_length=15, default=code, verbose_name='Проверочный код')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
