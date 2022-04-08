from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Product, Customer, Order, OrderItem

# Create your views here.


def shop(request):
    """ A view to return the shop page"""

    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/shop.html', context)


def cart(request):
    """ A view to return the cart page"""

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        # create empty cart for now for non-logged in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    """ A view to return the checkout page"""

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        # create empty cart for now for non-logged in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'shop/checkout.html', context)


def updateItem(request):
    """ if you add an item to the cart"""

    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    print('productId', productId)
    print('Action', action)
    return JsonResponse('Item was added', safe=False)
