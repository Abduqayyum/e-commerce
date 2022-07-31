from urllib.robotparser import RequestRate
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from store.models import Product, Card, OrderItem, Order
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def index(request):
    orders = Order.objects.filter(user=request.user)
    data = {
        "orders": orders
    }
    return render(request, "store/orders/index.html", data)

@login_required(login_url="login")
def vieworder(request, tr_no):
    order = Order.objects.filter(tracking_no=tr_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    data = {
        "orderitems": orderitems,
        "order": order
    }
    return render(request, "store/orders/view.html", data)