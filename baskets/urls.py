from django.urls import path
from baskets.views import baskets


urlpatterns = [
    path('', baskets, name='basket'),

]