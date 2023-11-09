from django.urls import path
from . import views
from products.views import (index, products, category_products_view, detail_view, about, detail_view_index, contacts,
                            search_results)

urlpatterns = [
    path('', index, name='index'),  # Отображение главной страницы
    path('products/', products, name='products'),  # Отображение страницы с продуктами
    # path('basket/', baskets, name='basket'),
    path('product/<int:id>/', detail_view, name='details'),  # Отображение детализации продукции продукты
    path('product/<int:id>/', detail_view_index, name='details_index'),  # Отображение детализации продукции главная
    path('about/', about, name='about'),  # Отображение информации о компании
    path('contact/', contacts, name='contact'),  # Отображение информации о компании
    path('products/category/<int:category_id>/', category_products_view, name='category_products'),  # Категории
    path('search/products/', search_results, name='search_results'),

]
