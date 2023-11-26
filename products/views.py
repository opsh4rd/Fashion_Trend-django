from datetime import date

from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings

from baskets.models import Baskets
from products.forms import SendMessage
from products.models import Newsletter
from products.models import Product, ProductCategory


# Главная
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


# Страницы с продуктами
def products(request, page_number=1):
    products = Product.objects.all()

    per_page = 8
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'title': 'Products',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
        'baskets': baskets,

    }
    return render(request, 'products/products.html', context)


# Категории на странице с продуктами
def category_products_view(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    categories = ProductCategory.objects.all()
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'title': 'Products',
        'baskets': baskets,
    }
    return render(request, 'products/products.html', context)


# Детализации продукции на странице 'Продукты'
def detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    size = product.choices.all()
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'size': size,
        'title': 'Product Detail',
        'product': product,
        'categories': ProductCategory.objects.all(),
        'baskets': baskets,
    }
    return render(request, 'products/product-detail.html', context)


# Детализации продукции на странице 'Главная'
def detail_view_index(request, id):
    product = get_object_or_404(Product, id=id)
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'title': 'Product Detail',
        'product': product,
        'categories': ProductCategory.objects.all(),
        'baskets': baskets,
    }
    return render(request, 'products/product-detail.html', context)


# Информации о компании
def about(request):
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'title': 'About',
        'baskets': baskets,
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/about.html', context)


# Контакты
def contacts(request):
    if request.method == 'POST':
        form = SendMessage(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['email'], form.cleaned_data['text'])

    else:
        form = SendMessage()

    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'title': 'Contact',
        'baskets': baskets,
        'categories': ProductCategory.objects.all(),
        'form': form,
    }
    return render(request, 'products/contacts.html', context)


# Обратная связь в 'контактах'
def send_message(email, text_message):
    text = get_template('products/messages.html')
    html = get_template('products/messages.html')
    context = {'text_message': text_message, 'email': email}
    subject = 'Сообщение от пользователя'
    from_email = settings.EMAIL_HOST_USER
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


# Поиск товаров
def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)

    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'query': query,
        'products': products,
        'title': 'Products',
        'baskets': baskets,
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

    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'products': products,
        'title': 'Products',
        'baskets': baskets,
        'categories': ProductCategory.objects.all(),

    }

    return render(request, 'products/products.html', context)


# Сортировка по возрастанию
def sort_by_low_to_high(request):
    products = Product.objects.order_by('price')

    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'products': products,
        'title': 'Products',
        'baskets': baskets,
        'categories': ProductCategory.objects.all(),

    }

    return render(request, 'products/products.html', context)


# Сортировка по убыванию
def sort_by_high_to_low(request):
    products = Product.objects.order_by('-price')
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'products': products,
        'title': 'Products',
        'baskets': baskets,
        'categories': ProductCategory.objects.all(),

    }

    return render(request, 'products/products.html', context)


# Имитация сортировка по последним добавленным элементам с index (по сезону)
def product_category_index_year(request, category_id):
    products = Product.objects.filter(Q(category=category_id) & Q(date__gte=date(2023, 11, 10)))
    categories = ProductCategory.objects.all()
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'products': products,
        'title': 'Products',
        'baskets': baskets,
        'categories': categories

    }
    return render(request, 'products/products.html', context)


# Подписка на новости
def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем данные из HTML-формы напрямую
        if email:  # Проверяем, что email не пустой
            Newsletter.objects.create(email=email)  # Создаем новый объект модели на основе полученных данных
            return HttpResponseRedirect(
                '/')  # Перенаправляем пользователя на главную страницу после успешной отправки данных
    return render(request, 'products/base.html')
