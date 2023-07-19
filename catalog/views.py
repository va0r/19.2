from django.shortcuts import render

from catalog.models import Category, Product


def index(request, *args, **kwargs):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог',
        'description': 'Приложение для работы с категориями и товарами',
        'flag': False
    }
    return render(request, 'catalog/index.html', context)


def categories(request, *args, **kwargs):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Каталог',
        'description': 'Список категорий',
        'flag': True
    }
    return render(request, 'catalog/categories.html', context)


def category_products(request, pk, *args, **kwargs):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': 'Каталог',
        'description': f'Список товаров категории {category_item.title}',
        'flag': False
    }
    return render(request, 'catalog/products.html', context)


def products(request, *args, **kwargs):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог',
        'description': 'Список товаров',
        'flag': False
    }
    return render(request, 'catalog/products.html', context)


def contacts(request, *args, **kwargs):
    context = {
        'title': 'Каталог',
        'description': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
