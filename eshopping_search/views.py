from django.db.models import Q

from django.shortcuts import render

from eshopping_app.models import products_db


def eshop_search(request):
    query = None
    products = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = products_db.objects.all().filter(Q(name__contains=query) | Q(details__contains=query))
    return render(request, 'shopping_search.html', dict(products=products, query=query))