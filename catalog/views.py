from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Contact, Version


class IsPublishedMixin:

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class IndexListView(LoginRequiredMixin, IsPublishedMixin, ListView):
    model = Product

    extra_context = {
        'title': 'Каталог',
        'description': 'Приложение для работы с категориями и товарами',
        'cropped': True
    }


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    extra_context = {
        'title': 'Каталог',
        'description': 'Список категорий',
        'is_product': True
    }


class CategoryProductListView(LoginRequiredMixin, IsPublishedMixin, ListView):
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


class ProductListView(LoginRequiredMixin, IsPublishedMixin, ListView):
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    extra_context = {
        'title': 'Каталог',
        'description': 'Добавление товара'
    }

    def form_valid(self, form):
        self.object = form.save()
        self.object.seller = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    extra_context = {
        'title': 'Каталог',
        'description': 'Изменение товара'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
