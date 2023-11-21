from django.db import models


# Категории
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


# Размеры
class Choices(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# Продукты
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    choices = models.ManyToManyField(Choices)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='products_image')
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


# Подписка на рассылки
class Newsletter(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
