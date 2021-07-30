from django.shortcuts import render
from .models import *


    
def home(request):
    
    return render(request, 'all_products/home.html',)
      
def store(request):
   products = Product.objects.all()
   print(products)
   context = {'products':products}
	
   return render(request, 'all_products/store.html',context)
   
def cart(request):
   if request.user.is_authenticated:
         customer = request.user.customer
         order, created = Order.objects.get_or_create(customer=customer)
         items = order.orderitem_set.all()

   context = {'items':items, 'order':order}
   return render(request, 'all_products/cart.html', context)

def checkout(request):
   if request.user.is_authenticated:
         customer = request.user.customer
         order, created = Order.objects.get_or_create(customer=customer)
         items = order.orderitem_set.all()

   context = {'items':items, 'order':order}
   return render(request, 'all_products/checkout.html', context)