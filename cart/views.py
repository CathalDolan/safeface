from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


# View the cart
def view_cart(request):

    return render(request, 'cart/cart.html')


# Add a product to the cart
def add_to_cart(request, item_id):

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    # Update the existing session
    request.session['cart'] = cart
    return redirect(redirect_url)


# Update the cart Qty from the Cart page
def update_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    print(quantity)
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'{product.name} removed from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# Delete an Item from the Cart page
def delete_from_cart(request, item_id):

    try:
        cart = request.session.get('cart', {})
        product = get_object_or_404(Product, pk=item_id)
        cart.pop(item_id)
        messages.success(request, f'{product.name} removed from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing it: {e}')
        return HttpResponse(status=500)
