from django.urls import path
from .views import *

urlpatterns = [
    path('',homeview,name='home'),
    path('cart/',cartView,name='cart'),
    path('add/<int:pk>',addView,name='add-item'),
    path('deleTE/<int:pk>',removeView,name='del-item'),
    path('view/<int:pk>',viewItem,name='view-item'),
    
    path('login/',signinView,name='login'),
    path('logout/',logoutView,name='logout'),
    path('register/',registerView,name='register'),
    
]
