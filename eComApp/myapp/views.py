from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cart_items = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cart_items': cart_items}
    return render(request, 'store/store.html', context)

def cart(request):
    print(request.user)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cart_items = order['get_cart_items']

    context = {'items':items, 'order':order, 'cart_items': cart_items}
    return render(request, 'store/cart.html', context)

@csrf_exempt
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cart_items = order['get_cart_items']

    context = {'items':items, 'order':order, 'cart_items': cart_items}
    return render(request, 'store/checkout.html', context)

def update_item(request):

    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    print(product_id)
    print(action)
    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = order_item.quantity + 1
    elif action == 'remove':
         order_item.quantity = order_item.quantity - 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)

@csrf_exempt
def processOrder(request):
    print("Data: ", request.body)
    return JsonResponse('Payment complete', safe=False)
