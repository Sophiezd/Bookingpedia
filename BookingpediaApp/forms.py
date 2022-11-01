from django import forms
from .models import Customer, Room, Hotel, Reservation, Item, Transaction


class CustomerEditForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    bill = forms.FloatField(label='Bill')

class HotelEditForm(forms.Form):
    name = forms.CharField(label='Hotel Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)

class RoomEditForm(forms.Form):
    type = forms.CharField(label='Room Type', max_length=100)
    price = forms.FloatField(label='Room Price')
    hotel = forms.ModelChoiceField(queryset = Hotel.objects.all())

class ReservationEditForm(forms.Form):
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
    room = forms.ModelChoiceField(queryset = Room.objects.all())
    customer = forms.ModelChoiceField(queryset = Customer.objects.all())

class ItemEditForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    price = forms.FloatField(label='price')

class TransactionEditForm(forms.Form):
    timestamp = forms.DateTimeField(label='Purchased At')
    count = forms.FloatField(label='Number Purchased')
    item = forms.ModelChoiceField(queryset = Item.objects.all())
    room = forms.ModelChoiceField(queryset = Room.objects.all())
    customer = forms.ModelChoiceField(queryset = Customer.objects.all())