
from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput,TextInput
from .models import Records


#-- registration from (create a user)

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # for field in ['username', 'password1', 'password2'] :
        #     self.fields[field].widget.attrs.update({
        #         'class': 'form-control',
        #         'placeholder':  f'Enter {field}'
        #     })
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Re-enter password'
        })
       
        
#-- login form ( login a user )  

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput(attrs={"class":"form-control" , "placeholder" : "Username"}))   
    password = forms.CharField(widget = PasswordInput(attrs={"class":"form-control" , "placeholder" : " Password"})) 
    
    
    
    
    
#-- Create a record (Add a record) 

class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model = Records
        fields = ['first_name','last_name','email','phone','adress','province','city','country']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your firstname'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your lastname'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your email'}) ,
            'phone' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your phone'}) ,
            'adress' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your adress'}), 
            'province' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your province'}),
            'city' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your city'}), 
            'country' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your country'}), 
        }
        

#-- update record

class UpdateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model = Records
        fields = ['first_name','last_name','email','phone','adress','province','city','country']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your firstname'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your lastname'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your email'}) ,
            'phone' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your phone'}) ,
            'adress' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your adress'}), 
            'province' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your province'}),
            'city' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your city'}), 
            'country' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your country'}), 
            
        }