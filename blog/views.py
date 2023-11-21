from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from baskets.models import Baskets
from blog.models import Blog, BlogCategories
from products.models import ProductCategory


# Блог
def blog(request, page_number=1):
    blogs = Blog.objects.all()

    per_page = 2
    paginator = Paginator(blogs, per_page)
    blogs_paginator = paginator.page(page_number)

    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'title': 'Blog',
        'blogs': blogs_paginator,
        'baskets': baskets,
        'categories_blog': BlogCategories.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'blog/blog.html', context)


# Детализация блога
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'title': 'Blog',
        'blog': blog,
        'baskets': baskets,
        'categories_blog': BlogCategories.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'blog/blog-detail.html', context)


# Категории блога
def category_blog(request, category_id):
    category = BlogCategories.objects.get(id=category_id)
    blogs = Blog.objects.filter(category=category)
    categories = BlogCategories.objects.all()
    context = {
        'category': category,
        'blogs': blogs,
        'categories_blog': categories,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'blog/blog.html', context)


# Поиск блога
def search_blogs(request):
    query = request.GET.get('q')
    blogs = Blog.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'blogs': blogs,
        'categories_blog': BlogCategories.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    if len(blogs) == 0:
        context['no_results'] = True

    return render(request, 'blog/blog.html', context)
