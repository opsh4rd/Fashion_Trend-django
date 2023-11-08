from django.urls import path
from . import views
from products.views import (index, products, category_products_view, detail_view, about, detail_view_index, contacts)

urlpatterns = [
    path('', index, name='index'),  # Отображение главной страницы
    path('products/', products, name='products'),  # Отображение страницы с продуктами
    # path('basket/', baskets, name='basket'),
    path('product/<int:id>/', detail_view, name='details'),  # Отображение детализации продукции
    path('product/<int:id>/', detail_view_index, name='details_index'),  # Отображение детализации продукции
    path('about/', about, name='about'),  # Отображение информации о компании
    path('contact/', contacts, name='contact'),  # Отображение информации о компании
    path('products/category/<int:category_id>/', category_products_view, name='category_products'),  # Категории
]
