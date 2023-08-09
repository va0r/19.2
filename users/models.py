from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    country = models.CharField(max_length=120, verbose_name='Страна', **NULLABLE)


    # TODO  https://my.sky.pro/student-cabinet/stream-lesson/84551/theory/5 03:52
