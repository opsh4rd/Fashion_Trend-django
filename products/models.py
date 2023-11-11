from django.db import models


class ProductCategory(models.Model):  # Категории товаров
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):  # Продукты
    CHOICES_SIZE = (
        ('Size S', 'S'),
        ('Size M', 'M'),
        ('Size L', 'L'),
        ('Size XL', 'XL'),
    )

    name = models.CharField(max_length=128)
    description = models.TextField()
    size = models.CharField(max_length=50, choices=CHOICES_SIZE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='products_image')
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:  # Отображение в админ панели
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
