from django.views.generic import ListView

from catalog.models import Category, Product, Contact


class IndexListView(ListView):
    model = Product

    extra_context = {
        'title': 'Каталог',
        'description': 'Приложение для работы с категориями и товарами',
        'cropped': True
    }


class CategoryListView(ListView):
    model = Category

    extra_context = {
        'title': 'Каталог',
        'description': 'Список категорий',
        'is_product': True
    }


class CategoryProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = 'Каталог'
        context_data['description'] = f'Список товаров категории {category_item.title}'
        return context_data


class ProductListView(ListView):
    model = Product

    extra_context = {
        'title': 'Каталог',
        'description': 'Список товаров',
    }


class ContactListView(ListView):
    model = Contact

    extra_context = {
        'title': 'Каталог',
        'description': 'Контакты'
    }
