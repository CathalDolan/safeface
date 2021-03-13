from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    product_total = 0
    product_count = 0
    products_total = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        product_total = quantity * product.price
        product_count += quantity
        products_total += product_total
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if products_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_PRICE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - products_total
    else:
        delivery = 0
        free_delivery_delta = 0

    net_total = products_total + delivery
    vat = net_total * Decimal(settings.VAT_RATE / 100)
    gross_total = net_total + vat

    context = {
        'cart_items': cart_items,
        'product_total': product_total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'sub_total': products_total,
        'net_total': net_total,
        'vat': vat,
        'gross_total': gross_total,
    }

    return context
