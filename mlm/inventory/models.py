from django.db import models
from django.utils import translation
from dashboard.models import *
from accounts.models import Profile
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20,blank=True, null=True,help_text="Enter Category")

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='product_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='product_updated')
    updated_at = models.DateTimeField(auto_now=True)
    firm = models.ForeignKey(FirmRegistration,on_delete=models.CASCADE,blank=True, null=True,related_name='firm_product')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    product_name = models.CharField(max_length=100,blank=True, null=True)
    product_image = models.ImageField(upload_to='product/image/',blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    cost_price = models.PositiveIntegerField(blank=True, null=True)
    selling_price = models.PositiveIntegerField(blank=True, null=True)
    product_active = models.BooleanField(default=False)
    product_description = models.TextField(blank=True, null=True)
    digital = models.BooleanField(default=False,blank=True, null=True)

    def __str__(self):
        return f"{self.product_name}"

    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ""
        return url 

    
class Order(models.Model):
    customer = models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,blank=True, null=True)
    transaction_id = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.quantity for item in orderitems)
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField(default=0,blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product.selling_price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200,blank=True, null=True)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


