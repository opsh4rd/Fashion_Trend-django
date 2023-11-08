from django.shortcuts import render, HttpResponseRedirect, reverse
# from django.contrib.auth.decorators import login_required
from products.models import Product
from baskets.models import Baskets
from products.models import ProductCategory


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


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Baskets.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Baskets.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return render(request, 'baskets/baskets.html')
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Baskets.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
