from django.contrib import admin

from blog.models import Blog, BlogCategories

admin.site.register(BlogCategories)
admin.site.register(Blog)
