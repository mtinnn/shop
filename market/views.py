from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import *

# Create your views here.


def homeview(request):
    items=Item.objects.all()
    context={}
    context['itemsList']=items
    return render(request,'home.html',context)



def cartView(request):

    if request.user.is_authenticated:
       customerr=request.user.customer
       orderr,created=Order.objects.get_or_create(customer=customerr,complete=False)
       items=orderr.orderitem_set.all()
       total=items.count()
       
    else:
       items=[]
    context={}
    context={'items':items,'orderr':orderr}
    
    
    return render(request,'cart.html',context)

def addView(request,pk):
    customerr=request.user.customer
    itemm = get_object_or_404(Item, pk=pk)
    order_item,created=OrderItem.objects.get_or_create(item=itemm)
    orderr,created=Order.objects.get_or_create(customer=customerr,complete=False)
    items=orderr.orderitem_set.all()
    order_qs = Order.objects.filter(customer=customerr, complete=False)
    if order_qs.exists():
       if items.filter(id=pk).exists():
          order_item.quantity+=1
          order_item.save()
       else:
          order_qs.item.add(order_item)
    else:
       order_date=timezone.now()
       order=Order.objects.create(user=request.user,date_order=order_date,)
       order.item.add(order_item)
       
          
          
    



def car(request,pk):
  pass

