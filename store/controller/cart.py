from urllib.robotparser import RequestRate
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from store.models import Product, Card
from django.contrib.auth.decorators import login_required

def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if Card.objects.filter(user=request.user.id, product_id=prod_id).exists():
                     return JsonResponse({"status": "Product already in Cart"})
                else:
                    prod_qty = int(request.POST.get("product_qty"))

                    if product_check.quantity >= prod_qty:
                        Card.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product added successfully"})
                    else:
                        return JsonResponse({"status": f"Only {product_check.quantity} quantity available"})
            else:
                return JsonResponse({"status": "No such product found"})
        else:
            return JsonResponse({"status": "Login to Continue"})
    return redirect("home")

@login_required(login_url="login")
def viewcart(request):
    carts = Card.objects.filter(user=request.user)
    data = {
        "carts": carts
    }
    return render(request, "store/cart.html", data)


def updatecart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get("product_id"))
        if Card.objects.filter(user=request.user, product_id=prod_id).exists():
            prod_qty = int(request.POST.get("product_qty"))
            cart = Card.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({"status": "Updated Successfully"})
    return redirect("home")


def deletecartitem(request):
    if request.method == "POST":
        prod_id = int(request.POST.get("product_id"))
        if Card.objects.filter(user=request.user, product_id=prod_id).exists():
            cartitem = Card.objects.get(user=request.user, product_id=prod_id)
            cartitem.delete()
            return JsonResponse({"status": "Deleted Successfully"})
    return redirect("home")



