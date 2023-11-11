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
        'categories_blog': BlogCategories.objects.all(),
        'categories': ProductCategory.objects.all(),  # Отображение категории в футере
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)

    context = {
        'title': 'Blog',
        'blog': blog,
        'baskets': Baskets.objects.filter(user=request.user),
        'categories_blog': BlogCategories.objects.all(),
        'categories': ProductCategory.objects.all(),  # Отображение категории в футере
    }

    return render(request, 'blog/blog-detail.html', context)


def category_blog(request, category_id):
    category = BlogCategories.objects.get(id=category_id)
    blogs = Blog.objects.filter(category=category)
    categories = BlogCategories.objects.all()
    context = {
        'category': category,
        'blogs': blogs,
        'categories_blog': categories,
        'categories': ProductCategory.objects.all(),
    }  # Отображение категории в футере}
    return render(request, 'blog/blog.html', context)


# Поиск блогов
def search_blogs(request):
    query = request.GET.get('q')
    blogs = Blog.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'blogs': blogs,
        'categories_blog': BlogCategories.objects.all(),
        'categories': ProductCategory.objects.all(),  # Отображение категории в футере
    }
    if len(blogs) == 0:
        context['no_results'] = True

    return render(request, 'blog/blog.html', context)
