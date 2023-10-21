from django.shortcuts import render


def index(request):
    context = {'title': 'Home'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Product'}
    return render(request, 'products/products.html', context)
