from django.urls import path
from baskets.views import baskets, basket_add, basket_remove, basket_negative

urlpatterns = [
    path('', baskets, name='basket'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),  # добавление в панели
    path('baskets/negative/<int:product_id>/', basket_negative, name='basket_negative'),  # убавление в панели
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),  # удаление в целом
]
