from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('catalog.Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Продавец')

    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.title} (цена: {self.price})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['pk']


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='categories/', **NULLABLE, verbose_name='Изображение')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']


class Contact(models.Model):
    key = models.CharField(max_length=25, verbose_name='Ключ')
    image = models.ImageField(upload_to='contacts/', **NULLABLE, verbose_name='')
    value = models.CharField(max_length=100, verbose_name='Значение')

    def __str__(self):
        return f'{self.key}: {self.value}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['pk']


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Название товара')
    number = models.SmallIntegerField(verbose_name='Номер версии')
    title = models.CharField(max_length=255, **NULLABLE, verbose_name='Название версии')
    description = models.TextField(**NULLABLE, verbose_name='Описание версии')
    is_active_version = models.BooleanField(verbose_name='Признак активной версии')

    def __str__(self):
        return f'Версия {self.number} ({self.product})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('number',)
