from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IVzTYB0ZTqMiCfI7Izt8XBTpQ2IFw6Opo1jBu9qeDorHfJO9wjz1jGOiBTrzaO7Ud57oVBcIbVqUEeuwzabVAdk00T2DkNwUr',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
