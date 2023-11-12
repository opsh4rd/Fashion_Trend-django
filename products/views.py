from django.db.models import Q
from django.shortcuts import render
from products.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from baskets.models import Baskets
from datetime import date


def index(request):
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'title': 'Home',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'baskets': baskets,
    }

    return render(request, 'products/index.html', context)


# Отображение страницы с продуктами
def products(request, category_id=None):
    context = {
        'title': 'Products',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
        'baskets': Baskets.objects.filter(user=request.user),

    }
    return render(request, 'products/products.html', context)


# Отображение категорий на странице с продуктами
def category_products_view(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    categories = ProductCategory.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'title': 'Products',
        'baskets': Baskets.objects.filter(user=request.user),
    }
    return render(request, 'products/products.html', context)


# Отображение детализации продукции на странице 'Продукты'
def detail_view(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        'title': 'Product Detail',
        'product': product,
        'categories': ProductCategory.objects.all(),
        'baskets': Baskets.objects.filter(user=request.user),
    }
    return render(request, 'products/product-detail.html', context)


# Отображение детализации продукции на странице 'Главная'
def detail_view_index(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        'title': 'Product Detail',
        'product': product,
        'categories': ProductCategory.objects.all(),
        'baskets': Baskets.objects.filter(user=request.user),
    }
    return render(request, 'products/product-detail.html', context)


# Отображение информации о компании
def about(request):
    context = {
        'title': 'About',
        'baskets': Baskets.objects.filter(user=request.user),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/about.html', context)


# Отображение контактов
def contacts(request):
    context = {
        'title': 'Contact',
        'baskets': Baskets.objects.filter(user=request.user),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/contacts.html', context)


# Поиск товаров
def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'products': products,
        'title': 'Products',
        'baskets': Baskets.objects.filter(user=request.user),
        'categories': ProductCategory.objects.all(),
    }
    if len(products) == 0:
        context['no_results'] = True

    return render(request, 'products/products.html', context)


# Сортировка по цене
def price_products(request, price_range):
    price_filters = {
        '0_50': {'price__lte': 50},
        '50_100': {'price__gt': 50, 'price__lte': 100},
        '100_150': {'price__gt': 100, 'price__lte': 150},
        '150_200': {'price__gt': 150, 'price__lte': 200},
        '200': {'price__gt': 200}
    }

    products = Product.objects.filter(**price_filters.get(price_range, {}))

    context = {
        'products': products,
        'title': 'Products',
        'baskets': Baskets.objects.filter(user=request.user),
        'categories': ProductCategory.objects.all(),

    }

    return render(request, 'products/products.html', context)


# Сортировка по возрастанию
def sort_by_low_to_high(request):
    products = Product.objects.order_by('price')
    context = {
        'products': products,
        'title': 'Products',
        'baskets': Baskets.objects.filter(user=request.user),
        'categories': ProductCategory.objects.all(),

    }

    return render(request, 'products/products.html', context)


# Сортировка по убыванию
def sort_by_high_to_low(request):
    products = Product.objects.order_by('-price')
    context = {
        'products': products,
        'title': 'Products',
        'baskets': Baskets.objects.filter(user=request.user),
        'categories': ProductCategory.objects.all(),

    }

    return render(request, 'products/products.html', context)


def product_category_index_year(request, category_id):
    products = Product.objects.filter(Q(category=category_id) & Q(date__gte=date(2023, 11, 10)))
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'title': 'Products',
        'baskets': Baskets.objects.filter(user=request.user),
        'categories': categories

    }
    return render(request, 'products/products.html', context)
