from django.shortcuts import render
from products.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from baskets.models import Baskets


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
    # Получаем объект категории по переданному идентификатору
    category = ProductCategory.objects.get(id=category_id)
    # Получаем все продукты, принадлежащие данной категории
    products = Product.objects.filter(category=category)
    # Получаем все категории для отображения ссылок
    categories = ProductCategory.objects.all()
    # Передаем объекты категории и товаров в контекст шаблона
    context = {'category': category, 'products': products, 'categories': categories}
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
    object_list = Product.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'object_list': object_list,
    }
    if len(object_list) == 0:
        context['no_results'] = True

    return render(request, 'products/search.html', context)


