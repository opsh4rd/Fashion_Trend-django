from django.urls import path

from baskets.views import (basket_add, basket_negative, basket_remove, baskets,
                           order)

urlpatterns = [
    path('', baskets, name='basket'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),  # добавление в панели
    path('negative/<int:product_id>/', basket_negative, name='basket_negative'),  # убавление в панели
    path('remove/<int:basket_id>/', basket_remove, name='basket_remove'),  # удаления в целом
    path('order/success/', order, name='order_success'),  # Принятие заказа
]
