from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.models import WishList, Product, Card
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def index(request):
    wishlist = WishList.objects.filter(user=request.user)
    data = {
        "wishlist": wishlist
    }
    return render(request, "store/wishlist.html", data)


def addtowishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if WishList.objects.filter(user=request.user, product_id=prod_id).exists():
                     return JsonResponse({"status": "Product already in Cart"})
                else:                   
                    WishList.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product added to Wishlist"})
            else:
                return JsonResponse({"status": "No such product found"})
        else:
            return JsonResponse({"status": "Login to Continue"})
    return redirect("home")


def deletewishlistitem(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            if WishList.objects.filter(user=request.user, product_id=prod_id).exists():
                wishlistitem = WishList.objects.get(user=request.user, product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({"status": "Product removed from wishlist"})
            else:
                return JsonResponse({"status": "Product not found in wishlist"})
        else:
            return JsonResponse({"status": "You are not logged in"})
    return redirect("home")



