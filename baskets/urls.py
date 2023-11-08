from django.urls import path
from baskets.views import baskets, basket_add, basket_remove

urlpatterns = [
    path('', baskets, name='basket'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
