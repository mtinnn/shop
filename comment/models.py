from django.db import models
from market.models import Customer,Item
# Create your models here.


class Comment(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text=models.CharField(max_length=200)
    time = models.TimeField(auto_now_add=True)




    def __str__(self):
        return str(self.item.name)
    




