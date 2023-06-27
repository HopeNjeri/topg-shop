from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .models import *
from brands.models import Product


@login_required(login_url='accounts:log_in')
def add_to_cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    items = order.orderitem_set.all()
    return render(request, 'add_to_cart.html', {"items": items, "order": order})


@login_required(login_url='accounts:log_in')
def check_out(request):
    customer = request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    items = order.orderitem_set.all()
    return render(request, 'check_out.html', {"items": items, "order": order})


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print("ProductId:", productId)
    print("Action:", action)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity < 1:
        orderItem.delete()

    return JsonResponse('item added successfully', safe=False)
