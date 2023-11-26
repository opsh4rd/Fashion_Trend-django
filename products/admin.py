from django.contrib import admin

from products.models import Choices, Newsletter, Product, ProductCategory

admin.site.register(ProductCategory)

admin.site.register(Choices)
admin.site.register(Newsletter)
admin.site.register(Product)


