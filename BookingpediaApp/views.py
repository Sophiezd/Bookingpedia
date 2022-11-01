from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Customer, Room, Hotel, Reservation, Item, Transaction


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers.html'
