from django.urls import path

from blog.views import blog, blog_detail, category_blog, search_blogs

urlpatterns = [
    path('', blog, name='blogs'),  # блог
    path('<int:id>', blog_detail, name='blog_details'),  # детализация блога
    path('category/<int:category_id>/', category_blog, name='category_blog'),  # категории блога
    path('page/<int:page_number>/', blog, name='paginator'),  # пагинация
    path('search/', search_blogs, name='search_blogs'),  # поиск блога
]
