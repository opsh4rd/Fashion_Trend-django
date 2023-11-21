from django.db import models

from products.models import Product
from users.models import User


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Baskets(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name} | Количество: {self.quantity}'

    def sum(self):
        return self.product.price * self.quantity


class Customer(models.Model):
    country = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    street = models.CharField(max_length=120)
    phone = models.CharField(max_length=50)
    baskets = models.ManyToManyField(Baskets, related_name='customers')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"заказ № {self.id}"
