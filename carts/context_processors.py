from .models import Cart, CartItem
from .views import _cart_id

def counters(request):
    cart_count = 0

    if 'admin' in request.path:
        return {}

    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart = Cart.objects.filter(cart_id=_cart_id(request)).first()
            cart_items = CartItem.objects.filter(cart=cart) if cart else []

        for cart_item in cart_items:
            cart_count += cart_item.quantity

    except Exception:
        cart_count = 0

    return dict(cart_count=cart_count)


