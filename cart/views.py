from django.shortcuts import render, redirect, reverse, HttpResponse


# View the cart
def view_cart(request):

    return render(request, 'cart/cart.html')


# Add a product to the cart
def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    # Update the existing session
    request.session['cart'] = cart
    return redirect(redirect_url)


# Update the cart Qty from the Cart page
def update_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# Delete an Item from the Cart page
def delete_from_cart(request, item_id):

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
