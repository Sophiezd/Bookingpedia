from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Customer, Room, Hotel, Reservation, Item, Transaction


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers.html'

class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels.html'

class RoomListView(ListView):
    model = Room
    template_name = 'rooms.html'

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservations.html'

class ItemListView(ListView):
    model = Item
    template_name = 'items.html'

class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions.html'