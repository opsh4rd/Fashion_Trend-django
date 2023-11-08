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
    get_category = BlogCategories.objects.get(id=category_id)
    filter_blog = Blog.objects.filter(category=get_category)
    categories_all = BlogCategories.objects.all()
    context = {'get_category': get_category, 'filter_blog': filter_blog, 'categories_all': categories_all}
    return render(request, 'blog/blog.html', context)
