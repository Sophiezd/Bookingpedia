from django import forms
from .models import Customer, Room, Hotel, Reservation, Item, Transaction


class CustomerEditForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    bill = forms.FloatField(label='bill')

class HotelEditForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    address = forms.CharField(label='address', max_length=100)

class RoomEditForm(forms.Form):
    type = forms.CharField(label='name', max_length=100)
    price = forms.FloatField(label='price')
    hotel = forms.ModelMultipleChoiceField(queryset = Hotel.objects.all())

class ReservationEditForm(forms.Form):
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
    room = forms.ModelMultipleChoiceField(queryset = Room.objects.all())
    customer = forms.ModelMultipleChoiceField(queryset = Customer.objects.all())

class ItemsEditForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    price = forms.FloatField(label='price')

class TransactionEditForm(forms.Form):
    timestamp = forms.DateTimeField(label='Purchased At')
    count = forms.FloatField(label='Number Purchased')
    item = forms.ModelMultipleChoiceField(queryset = Item.objects.all())
    room = forms.ModelMultipleChoiceField(queryset = Room.objects.all())
    customer = forms.ModelMultipleChoiceField(queryset = Customer.objects.all())