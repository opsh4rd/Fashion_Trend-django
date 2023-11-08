from django.db import models


class BlogCategories(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Категорию блога'
        verbose_name_plural = 'Категории блога'

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_image')
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(to=BlogCategories, on_delete=models.CASCADE)

    class Meta:  # Отображение в админ панели
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
