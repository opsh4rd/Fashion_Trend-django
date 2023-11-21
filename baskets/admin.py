from django.contrib import admin

from baskets.models import Baskets, Customer

admin.site.register(Customer)


class BasketsAdmin(admin.TabularInline):
    model = Baskets
    fields = ('product', 'quantity')
    extra = 0
