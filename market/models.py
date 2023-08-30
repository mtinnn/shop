from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    image=models.ImageField(null=True, blank=True)
    name=models.CharField(max_length=100)
    information=models.CharField(max_length=200)
    count=models.IntegerField(null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)

  

    
    

    def __str__(self):
        return str(self.name)
    

class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE,related_name='customer')
    name=models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    customer=models.OneToOneField(Customer, null=True,blank=True, on_delete=models.CASCADE)
    date_order=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True)
    transaction_id=models.IntegerField(null=True)

    @property
    def get_total_cart(self):
        
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    def get_item_cart(self):

        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total


    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    item=models.ForeignKey(Item, null=True, blank=True, on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,blank=True,on_delete=models.SET_NULL )
    quantity=models.IntegerField(default=0,null=True,blank=True)
    dateAdded=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)

    @property
    def get_total(self):
        total=int(self.item.price)*int(self.quantity)
        return total
        
    def __str__(self) :
        return str(self.item)




