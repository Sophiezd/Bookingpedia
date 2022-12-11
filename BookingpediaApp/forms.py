from django import forms
from .models import Customer, Room, Hotel, Item


class CustomerEditForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username', max_length=100)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Password (Blank keeps old password)', max_length=100, required=False)
    bill = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Bill')

class HotelEditForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Hotel Name', max_length=100)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Address', max_length=100)

class RoomEditForm(forms.Form):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Room Number')
    type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Room Type', max_length=100)
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Room Price')
    hotel = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Hotel.objects.all())

class ReservationEditForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Start Date')
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='End Date')
    room = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Room.objects.all())
    customer = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Customer.objects.all())

class ItemEditForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='name', max_length=100)
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='price')

class TransactionEditForm(forms.Form):
    timestamp = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}), label='Purchased At')
    count = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Number Purchased')
    item = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Item.objects.all())
    room = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Room.objects.all())
    customer = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Customer.objects.all())

class PayBillForm(forms.Form):
    payment = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Bill')