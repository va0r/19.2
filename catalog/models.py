from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('catalog.Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.price}'

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


class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=250, **NULLABLE, verbose_name='Slug')
    content = models.TextField(max_length=1000, verbose_name='Содержание')
    image = models.ImageField(upload_to='categories/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cnt_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f''

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ('pk',)
