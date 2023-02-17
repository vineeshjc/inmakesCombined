from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from eshopping_app.models import products_db
from eshopping_cart_app.models import e_cart, e_cart_item


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = products_db.objects.get(id=product_id)
    try:
        cart = e_cart.objects.get(cart_id=_cart_id(request))
    except e_cart.DoesNotExist:
        cart = e_cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_items = e_cart_item.objects.get(product=product, cart=cart)
        if cart_items.quantity < cart_items.product.stock:
            cart_items.quantity += 1
        cart_items.save()
    except e_cart_item.DoesNotExist:
        cart_items = e_cart_item.objects.create(product=product, quantity=1, cart=cart)
        cart_items.save()
    return redirect('shopping_cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = e_cart.objects.get(cart_id=_cart_id(request))
        cart_items = e_cart_item.objects.filter(cart=cart, item_status=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'shopping_cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_item_quantity(request, product_id):
    cart = e_cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(products_db, id=product_id)
    cart_item = e_cart_item.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('shopping_cart:cart_detail')


def cart_item_delete(request, product_id):
    cart = e_cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(products_db, id=product_id)
    cart_item = e_cart_item.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('shopping_cart:cart_detail')
