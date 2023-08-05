from django.contrib import admin

from catalog.models import Product, Category, Contact, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'key', 'value')
    search_fields = ('title',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'number', 'is_active')
    search_fields = ('title', 'product')
