from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):

    products = Product.objects.all()
    # Needed for Search
    query = None
    # Needed for categories
    categories = None

    # Categories
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Search functionality in Navbar
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # Connected with "except Exception as e:" in bag views.py
                messages.error(request, "You didn't tell us what you're looking for")
                return redirect(reverse('products'))
            
            # Q allows us to query the product name and description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
