from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import IndexListView, CategoryListView, ProductListView, CategoryProductListView, \
    ContactListView, ProductCreateView, ProductUpdateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    # главная
    path('', IndexListView.as_view(), name='index'),
    # все категории
    path('categories/', CategoryListView.as_view(), name='categories'),
    # все товары
    path('products/', ProductListView.as_view(), name='products'),
    # контакты
    path('contacts/', ContactListView.as_view(), name='contacts'),

    # все товары по выбранной категории
    path('categories/<int:pk>/products/', CategoryProductListView.as_view(), name='category_products'),
    # создание товара
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    # просмотр товара
    path('products/read/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='read_product'),
    # изменение товара
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]
