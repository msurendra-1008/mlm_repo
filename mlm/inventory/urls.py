from django.urls import path
from .views import *


urlpatterns = [
    path('gallery/',product_gallery,name="gallery"),
    path('gallery_product_detail/<int:pk>/',gallery_detail,name="gallery-product-detail"),
    path('create_product/',create_product,name="create-product"),
    path('product_list/',product_list,name="product-list"),
    path('cart/',cart,name="cart"),
	path('checkout/',checkout,name="checkout"),
	path('update_item/',updateItem,name="update_item"),
	path('process_order/',processOrder,name="process_order"),


]