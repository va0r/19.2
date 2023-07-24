from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexListView, contacts, CategoryListView, ProductListView, CategoryProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/products', CategoryProductListView.as_view(), name='category_products'),
    path('products/', ProductListView.as_view(), name='products'),
    path('contacts/', contacts, name='contacts'),
]