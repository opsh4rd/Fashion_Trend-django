from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
# from django.contrib.auth.decorators import login_required
from products.models import Product
from baskets.models import Baskets
from products.models import ProductCategory


# Отображение корзины товаров
def baskets(request):
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user)
    else:
        baskets = []

    context = {
        'title': 'Shopping Cart',
        'baskets': baskets,
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'baskets/baskets.html', context)


# Добавление и прибавление товара
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Baskets.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Baskets.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Убавление товара
def basket_negative(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Baskets.objects.filter(user=request.user, product=product)

    if baskets.exists():
        basket = baskets.first()
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Удаление в целом товара
def basket_remove(request, basket_id):
    basket = Baskets.objects.get(id=basket_id)
    baskets = Baskets.objects.filter(user=request.user)
    del_basket = basket.delete()
    context = {
        'del_basket': del_basket,
        'baskets': baskets,
    }

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
