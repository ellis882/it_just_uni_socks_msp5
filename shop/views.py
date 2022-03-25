from django.shortcuts import render

# Create your views here.
def shop(request):
    """ A view to return the shop page"""
    context = {}
    return render(request, 'shop/shop.html', context)

def cart(request):
    """ A view to return the cart page"""
    context = {}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    """ A view to return the checkout page"""
    context = {}
    return render(request, 'shop/checkout.html', context)
