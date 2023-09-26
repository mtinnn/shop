from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from comment.models import Comment



class registerForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password '}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                
                'placeholder':'username'
                }),
                'email': forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder':'email'
                }),


                
                }
  

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username '}))
    password= forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password '}))

    class Meta:
        model=User
        fields=['username', 'password']

class newCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','text']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
             

         }



    