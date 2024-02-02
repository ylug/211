from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_for_one', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'views_count',)
    list_filter = ('is_published', 'views_count',)
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')
    list_filter = ('product',)