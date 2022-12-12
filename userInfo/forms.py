from django import forms
from django.contrib.auth.forms import UserCreationForm
from BookingpediaApp.models import Customer

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ("username",)