from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    slug = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    image= models.ImageField(upload_to="images", blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    product_image= models.ImageField(upload_to="images", blank=False, null=False)
    small_description = models.CharField(max_length=250, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    orginal_price = models.FloatField(blank=False, null=False)
    selling_price = models.FloatField(blank=False, null=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    tag = models.CharField(max_length=100, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    orderstatuser = (
        ("Pending", "Pending"),
        ("Out for Shipping", "Out for Shipping"),
        ("Completed", "Completed")
    )
    status = models.CharField(max_length=150, choices=orderstatuser, default="Pending")
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.id}, {self.tracking_no}"

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.order.id}, {self.order.tracking_no}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username