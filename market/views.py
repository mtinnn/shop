from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate,logout
from django.views.generic import CreateView
from .models import *
from.forms import *
from comment.models import Comment


# Create your views here.



def homeview(request):
    items=Item.objects.all()
    if request.user.is_authenticated:
       customerr=request.user.customer
       orderr,created=Cart.objects.get_or_create(customer=customerr,complete=False)

    else:
       orderr={'get_total_cart':0,'get_item_cart':0}
       
       

       
    context={}
    context={'itemsList':items,'orderr':orderr}
    
    return render(request,'home.html',context)



def cartView(request):

    if request.user.is_authenticated:
       customerr=request.user.customer
       orderr,created=Cart.objects.get_or_create(customer=customerr,complete=False)
       items=orderr.orderitem_set.all()
    else:
       items=[]
       orderr={'get_total_cart':0,'get_item_cart':0}
    context={}
    context={'items':items,'orderr':orderr}

    return render(request,'cart.html',context)



def addView(request,pk):
  customerr=request.user.customer

  orderr,created=Cart.objects.get_or_create(customer=customerr,complete=False)
  item,createdd=OrderItem.objects.get_or_create(item_id=pk,order=orderr)
  item.quantity+=1
  item.save()

  return redirect('cart')
  
def removeView(request,pk):
  item=OrderItem.objects.get(id=pk)
  item.quantity-=1
  item.save()
  if  item.quantity==0:
     item.delete()
     
 
  return redirect('cart')
        
    

def viewItem(request,pk):
  comments=Comment.objects.filter(item_id=pk)
  item=Item.objects.get(id=pk)
  user_comment=None
  if request.method  == 'POST':
     customerr=request.user.customer
     comment_form=newCommentForm(request.POST)
     if comment_form.is_valid():
        user_comment=comment_form.save(commit=False)
        user_comment.item=item
        user_comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
  else:
     comment_form=newCommentForm()

     
            
  return render(request,'item.html',{"item":item,'comments':comments,'form':comment_form})

        
  




def registerView(request):

   form=registerForm()

   if request.method=='POST':
      form=registerForm(request.POST)
      if form.is_valid():
         form.save()

   context={'form':form}
   return render(request,'registration/register.html',context)


def signinView(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'registration/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                
                return redirect('home')
        
        error={'text':'Invalid username or password'}
        return render(request,'registration/login.html',{'form': form,'error':error})
   
     




def logoutView(request):
   logout(request)
   return redirect('home')  