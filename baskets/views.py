from django.shortcuts import render


def baskets(request):
    context = {
        'title': 'Shoping Cart',
    }
    return render(request, 'baskets/baskets.html', context)
