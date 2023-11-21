from django.contrib import admin

from products.models import Choices, Newsletter, Product, ProductCategory

admin.site.register(ProductCategory)

admin.site.register(Choices)
admin.site.register(Newsletter)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    fields = ('name', 'description', 'quantity', 'price', 'image', 'category')
    search_fields = ('name',)
    ordering = ('name',)
