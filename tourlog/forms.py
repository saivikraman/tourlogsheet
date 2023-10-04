from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Datas
from .models import Detail



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class DatasForm(forms.ModelForm):
    class Meta:
        model = Datas
        fields = '__all__'  

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__' 

