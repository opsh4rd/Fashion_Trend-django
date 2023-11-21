from django.urls import path

from products.views import (about, category_products_view, contacts,
                            detail_view, detail_view_index, index, newsletter,
                            price_products, product_category_index_year,
                            products, search_results, sort_by_high_to_low,
                            sort_by_low_to_high)

urlpatterns = [
    path('', index, name='index'),  # Главная страница
    path('products/', products, name='products'),  # Продукты
    path('product/<int:id>/', detail_view, name='details'),  # Детализация
    path('product/<int:id>/', detail_view_index, name='details_index'),  # Детализация главная
    path('about/', about, name='about'),  # О компании
    path('contact/', contacts, name='contact'),  # Контакты
    path('category/<int:category_id>/products/', category_products_view, name='category_products'),  # Категории
    path('search/products/', search_results, name='search_results'),  # Поиск товаров
    path('products/page/<int:page_number>/', products, name='paginator_products'),  # Пагинация
    path('product/filter/price/<str:price_range>/', price_products, name='price_products'),  # Фильтр по ценам
    path('product/filter/sort/asc', sort_by_low_to_high, name='sort_by_low_to_high'),  # Фильтр по возрастанию
    path('product/filter/sort/desc', sort_by_high_to_low, name='sort_by_high_to_low'),  # Фильтр по убыванию
    path('newsletter/', newsletter, name='newsletter'),  # Подписка на новости
    path('category/<int:category_id>/products/trend', product_category_index_year, name='product_category_index_year'),
    # Имитация по новым продуктам(сезонность)
]
