from django.urls import path
from .views import *
urlpatterns = [
    path('',homeview,name='home'),
    path('cart/',cartView,name='cart'),
    path('add/<int:pk>',addView,name='add-item')
    
]
