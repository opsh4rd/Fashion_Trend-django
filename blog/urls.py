from django.urls import path
from blog.views import blog, blog_detail, category_blog


urlpatterns = [
    path('', blog, name='blogs'),
    path('<int:id>', blog_detail, name='blog_details'),
    path('category/<int:category_id>/', category_blog, name='category_blog'),  # Категории
]
