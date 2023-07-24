from django.contrib import admin

from catalog.models import Product, Category, Contact, Note


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'key', 'value')
    search_fields = ('title',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'is_published', 'cnt_views')
    list_filter = ('title', 'content')
    search_fields = ('title', 'content')
