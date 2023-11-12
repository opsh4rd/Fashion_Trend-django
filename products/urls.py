from django.urls import path
from . import views
from products.views import (index, products, category_products_view, detail_view, about, detail_view_index, contacts,
                            search_results, price_products, sort_by_low_to_high, sort_by_high_to_low,
                            product_category_index_year)

urlpatterns = [
    path('', index, name='index'),  # Отображение главной страницы
    path('products/', products, name='products'),  # Отображение страницы с продуктами
    path('product/<int:id>/', detail_view, name='details'),  # Отображение детализации продукции продукты
    path('product/<int:id>/', detail_view_index, name='details_index'),  # Отображение детализации продукции главная
    path('about/', about, name='about'),  # Отображение информации о компании
    path('contact/', contacts, name='contact'),  # Отображение информации о компании
    path('category/<int:category_id>/products/', category_products_view, name='category_products'),  # Категории
    path('search/products/', search_results, name='search_results'),  # Поиск
    path('product/filter/price/<str:price_range>/', price_products, name='price_products'),  # Фильтр цена
    path('product/filter/sort/asc', sort_by_low_to_high, name='sort_by_low_to_high'),  # Фильтр сортировки о возрастанию
    path('product/filter/sort/desc', sort_by_high_to_low, name='sort_by_high_to_low'),  # Фильтр сортировки по убыванию
    path('category/<int:category_id>/products/trend', product_category_index_year, name='product_category_index_year'),
    # Категории


]
