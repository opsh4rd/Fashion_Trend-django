from django.shortcuts import render
from baskets.models import Baskets
from blog.models import Blog, BlogCategories
from django.shortcuts import get_object_or_404
from products.models import ProductCategory


def blog(request):
    context = {
        'title': 'Blog',
        'blogs': Blog.objects.all(),
        'baskets': Baskets.objects.filter(user=request.user),
        'BlogCategories': BlogCategories.objects.all(),
        'categories': ProductCategory.objects.all(),  # Отображение категории в футере
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)

    context = {
        'title': 'Blog',
        'blog': blog,
        'baskets': Baskets.objects.filter(user=request.user),
        'BlogCategories': BlogCategories.objects.all(),
        'categories': ProductCategory.objects.all(),  # Отображение категории в футере
    }

    return render(request, 'blog/blog-detail.html', context)


def category_blog(request, category_id):
    blog_category = BlogCategories.objects.get(id=category_id)
    blog_filter = Blog.objects.filter(category=blog_category)
    categories_all = BlogCategories.objects.all()
    context = {'blog_filter': blog_filter, 'categories_all': categories_all, 'blog_category': blog_category}
    return render(request, 'blog/blog_categories.html', context)


# Поиск блогов
def search_blogs(request):
    query = request.GET.get('q')
    object_list = Blog.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'object_list': object_list,
        'BlogCategories': BlogCategories.objects.all(),
    }
    if len(object_list) == 0:
        context['no_results'] = True

    return render(request, 'blog/blog_search.html', context)
