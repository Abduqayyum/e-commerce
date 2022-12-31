from django.urls import path
from . import views
from .controller import authView, cart, wishlist, checkout, order


urlpatterns = [
    path("", views.home, name="home"),
    path("collections", views.collections, name="collections"),
    path("collections/<slug:slug>", views.collectionsview, name="collectionsview"),
    path("collections/<slug:cate_slug>/<slug:prod_slug>", views.productview, name="productview"),

    path("product-list", views.productslist, name="productlist"),
    path("searchproduct", views.searchproduct, name="searchproduct"),

    path("register", authView.register, name="register"),
    path("login", authView.loginpage, name="login"),
    path("logout", authView.logoutpage, name="logout"),

    path("add-to-cart", cart.addtocart, name="addtocart"),
    path("cart", cart.viewcart, name="cart"),
    path("update-cart", cart.updatecart, name="updatecart"),
    path("delete-cart-item", cart.deletecartitem, name="deletecartitem"),
    path("delete-wishlist-item", wishlist.deletewishlistitem, name="deletewishlistitem"),

    path("wishlist", wishlist.index, name="wishlist"),
    path("add-to-wishlist", wishlist.addtowishlist, name="addtowishlist"),
    path("checkout", checkout.index, name="checkout"),

    path("placeorder", checkout.placeorder, name="placeorder"),
    path("my-orders", order.index, name="myorders"),
    path("view-order/<str:tr_no>", order.vieworder, name="orderview")
]
