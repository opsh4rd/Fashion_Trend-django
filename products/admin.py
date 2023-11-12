from django.contrib import admin
from products.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'quantity', 'category')
    fields = ('name', 'description', 'size', 'quantity', 'price', 'image', 'category')
    search_fields = ('name',)
    ordering = ('name',)
