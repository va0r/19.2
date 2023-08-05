from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexListView, CategoryListView, ProductListView, CategoryProductListView, \
    ContactListView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),  # главная
    path('categories/', CategoryListView.as_view(), name='categories'),  # все категории
    path('products/', ProductListView.as_view(), name='products'),  # все товары
    path('contacts/', ContactListView.as_view(), name='contacts'),  # контакты

    path('categories/<int:pk>/products', CategoryProductListView.as_view(), name='category_products'),  # все товары по выбранной категории
    path('products/create/', ProductCreateView.as_view(), name='create_product'),  # создание товара
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),  # изменение товара

]
