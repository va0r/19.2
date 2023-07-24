from django.views.generic import ListView

from catalog.models import Category, Product, Contact


class IndexListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        # TODO: ограничить передаваемый контекст 100 элементами.
        # for item in queryset.iterator():
        #     item.description = item.description[:100] + '...'
        return queryset

    extra_context = {
        'title': 'Каталог',
        'description': 'Приложение для работы с категориями и товарами',
        'flag': False
    }


class CategoryListView(ListView):
    model = Category

    extra_context = {
        'title': 'Каталог',
        'description': 'Список категорий',
        'flag': True
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
        context_data['flag'] = False
        return context_data


class ProductListView(ListView):
    model = Product

    extra_context = {
        'title': 'Каталог',
        'description': 'Список товаров',
        'flag': False
    }


class ContactListView(ListView):
    model = Contact

    extra_context = {
        'title': 'Каталог',
        'description': 'Контакты'
    }
