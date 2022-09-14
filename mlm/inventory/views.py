from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
import datetime
# Create your views here.

from .models import *
from .forms import *

def create_product(request):
	page = "Create Product"
	form = CreateProductForm()
	if request.method == "POST":
		print(request.POST)
		form = CreateProductForm(request.POST,request.FILES)
		if form.is_valid():
			qs = form.save(commit=False)
			qs.created_by = request.user
			qs.product_active = True
			qs.save()
			return redirect('product_list')
	context = {'form':form,'page':page}
	return render(request,'inventory/create_product.html',context)

def product_list(request):
	products = Product.objects.all()
	print(products)
	context = {'products':products}
	return render(request,'dashboard/product_list.html',context)

def product_gallery(request):
	if request.user.is_authenticated:
		customer = request.user.profile
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']
	products = Product.objects.filter(product_active = True)

	context = {'products':products,'cartItems':cartItems,'items':items}
	return render(request,'inventory/gallery.html',context)

def gallery_detail(request,pk):
	product_details = Product.objects.get(pk=pk)
	context = {'product_details':product_details}
	return render(request,'inventory/gallery_detail.html',context)


def cart(request):
	if request.user.is_authenticated:
		customer = request.user.profile
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']
	context = {'items':items,'order':order,'cartItems':cartItems}
	return render(request, 'inventory/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.profile
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']
	context = {'items':items,'order':order,'cartItems':cartItems}
	return render(request, 'inventory/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	
	customer = request.user.profile
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer,complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
	
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	else:
		orderItem.quantity = (orderItem.quantity - 1)
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added',safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	print(data)
	if request.user.is_authenticated:
		customer = request.user.profile
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id
		
		if total == order.get_cart_total:
			order.complete = True
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
				customer = customer,
				order = order,
				address = data['shipping']['address'],
				city = data['shipping']['city'],
				state = data['shipping']['state'],
				zipcode = data['shipping']['zipcode'],
			)
	else:
		print('user is not logged in!')
	return JsonResponse('Payment Complete!',safe=False)