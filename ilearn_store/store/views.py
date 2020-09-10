from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 


def basket(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_basket_total':0, 'get_basket_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'store/basket.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_basket_total':0, 'get_basket_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'store/checkout.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)
