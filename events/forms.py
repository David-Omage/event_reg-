from django.forms import ModelForm
from .models import Event, Applauders, SeatWarmers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['payment', 'hide']


class ApplaudersForm(ModelForm):
    class Meta:
        model = Applauders
        fields ='__all__'



class SeatWarmersForm(ModelForm):
    class Meta:
        model = SeatWarmers
        fields ='__all__'



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')