from django.urls import path
from blog.views import blog, blog_detail, category_blog, search_blogs


urlpatterns = [
    path('', blog, name='blogs'),
    path('<int:id>', blog_detail, name='blog_details'),
    path('category/<int:category_id>/', category_blog, name='category_blog'),  # Категории
    path('search/blogs/', search_blogs, name='search_blogs'),  # Категории
]
