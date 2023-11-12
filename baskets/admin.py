from django.contrib import admin
from baskets.models import Baskets


class BasketsAdmin(admin.TabularInline):
    model = Baskets
    fields = ('product', 'quantity')
    extra = 0
