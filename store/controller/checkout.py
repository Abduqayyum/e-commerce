import random
from urllib import response
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from store.models import WishList, Product, Card, Order, OrderItem, Profile

from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def index(request):
    rawcart = Card.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Card.objects.delete(id=item.id)
    
    cartitems = Card.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    userprofile = Profile.objects.filter(user=request.user).first()

    data = {
        "cartitems": cartitems,
        "total_price": total_price,
        "userprofile": userprofile
    }
    return render(request, "store/checkout.html", data)


# @login_required(login_url="login")
def placeorder(request):
    if request.method == "POST":
        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get("fname")
            currentuser.last_name = request.POST.get("lname")
            currentuser.save()
        
        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get("phone")
            userprofile.address = request.POST.get("address")
            userprofile.city = request.POST.get("city")
            userprofile.state = request.POST.get("state")
            userprofile.country = request.POST.get("country")
            userprofile.pincode = request.POST.get("pincode")
            print(f"sdsjdflsjfsjdf {request.POST.get('pincode')}")
            userprofile.save()


        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get("fname")
        neworder.lname = request.POST.get("lname")
        neworder.email = request.POST.get("email")
        neworder.phone = request.POST.get("phone")
        neworder.address = request.POST.get("address")
        neworder.city = request.POST.get("city")
        neworder.state = request.POST.get("state")
        neworder.country = request.POST.get("country")
        neworder.pincode = request.POST.get("pincode")

        neworder.payment_mode = request.POST.get("payment_mode")
        neworder.payment_id = request.POST.get("payment_id")


        cart = Card.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
        
        neworder.total_price = cart_total_price
        trackno = "Jack" + str(random.randint(111111,999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = "Jack" + str(random.randint(111111,999999))
        
        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Card.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(order=neworder, product=item.product, price=item.product.selling_price, quantity=item.product_qty)

            # to decrease the product quantity from available stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        # to clear user's Cart
        Card.objects.filter(user=request.user).delete()

        payMode = request.POST.get("payment_mode")
        if payMode == "Paid by Paypal":
            return JsonResponse({"status": "Your order has been placed successfully"})
        else:
            messages.success(request, "Your order has been placed successfully")

    return redirect("home")


