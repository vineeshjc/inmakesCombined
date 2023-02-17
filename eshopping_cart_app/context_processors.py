from eshopping_cart_app.models import e_cart_item, e_cart

from eshopping_cart_app.views import _cart_id


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = e_cart.objects.filter(cart_id=_cart_id(request))
            cart_items = e_cart_item.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except e_cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
