from django.contrib import admin
from users.models import User
from baskets.admin import BasketsAdmin


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketsAdmin,)
