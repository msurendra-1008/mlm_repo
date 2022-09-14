from django.contrib import admin

from .models import Category, Order, OrderItem,Product, ShippingAddress

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
