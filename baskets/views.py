from django.shortcuts import HttpResponseRedirect, render

from baskets.models import Baskets, Customer
from products.models import Product, ProductCategory


# Корзина товаров
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


# Добавления корзины
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


# Убавления корзины
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


# Удаления в целом
def basket_remove(request, basket_id):
    basket = Baskets.objects.get(id=basket_id)
    baskets = Baskets.objects.filter(user=request.user)
    del_basket = basket.delete()
    context = {
        'del_basket': del_basket,
        'baskets': baskets,
    }

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Заказ товаров
def order(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        state = request.POST.get('state')
        street = request.POST.get('street')
        phone = request.POST.get('phone')
        print(request.POST)

        customer = Customer.objects.create(
            country=country,
            state=state,
            street=street,
            phone=phone
        )

        baskets = Baskets.objects.filter(user=request.user)

        customer.baskets.set(baskets)

        return HttpResponseRedirect(
            '/')

    return render(request, 'baskets/baskets.html')
