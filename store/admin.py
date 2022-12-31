from django.contrib import admin
from .models import Product, Category, Card, WishList, Order, OrderItem, Profile
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Card)
admin.site.register(WishList)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Profile)
