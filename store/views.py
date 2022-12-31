from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Category, Product

# Create your views here.



def home(request):
    trending_products = Product.objects.filter(trending="1")
    data = {
        "trending_products" : trending_products
    }
    return render(request, "store/index.html", data)

def collections(request):
    categories = Category.objects.filter(status=0)
    data = {
        "categories": categories
    }
    return render(request, "store/collections.html", data)


def collectionsview(request, slug):
    if Category.objects.filter(slug=slug, status=0):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        data = {
            "products": products,
            "category_name": category_name
        }
        return render(request, "store/product/index.html", data)
    else:
        messages.warning(request, "No such category found")
        return redirect("collections")

    
def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            data = {
                "products": products
            }
        else:
            messages.error(request, "No such product found")
            return redirect("collections")
    else: 
        messages.error(request, "No such category found")
        return redirect("collections")
    return render(request, "store/product/view.html", data)


def productslist(request):
    products = Product.objects.filter(status=0).values_list("name", flat=True)
    productslist = list(products)
    return JsonResponse(productslist, safe=False)


def searchproduct(request):
    if request.method == "POST":
        searcheditem = request.POST.get("productsearch")
        if searcheditem == "":
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            product = Product.objects.filter(name__icontains=searcheditem).first()

            if product:
                return redirect('collections/' + product.category.slug + "/" + product.slug)
            else:
                messages.info(request, "No product matched your search")
                return redirect(request.META.get("HTTP_REFERER"))
                
    return redirect(request.META.get("HTTP_REFERER"))