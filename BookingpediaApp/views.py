from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Customer, Room, Hotel, Reservation, Item, Transaction
from django.http import HttpResponseRedirect, Http404
from .forms import CustomerEditForm, HotelEditForm, RoomEditForm, ReservationEditForm, ItemsEditForm, TransactionEditForm


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers.html'

class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels.html'

def insert_transaction(request):
    if request.method == 'POST':
        transaction = Reservation()
        transaction.timestamp = request.POST.get('timestamp')
        transaction.count = request.POST.get('count')
        transaction.item = request.POST.get('item')
        transaction.customer = request.POST.get('customer')
        transaction.room = request.POST.get('room')
        transaction.save()
        return redirect('/transactions')
    else:
        return render(request, 'insert_transaction.html')  

def insert_reservation(request):
    if request.method == 'POST':
        reservation = Reservation()
        reservation.start_date = request.POST.get('start_date')
        reservation.end_date = request.POST.get('end_date')
        reservation.room = request.POST.get('room')
        reservation.customer = request.POST.get('customer')
        reservation.save()
        return redirect('/reservations')
    else:
        return render(request, 'insert_reservation.html')  

def insert_room(request):
    if request.method == 'POST':
        room = Room()
        room.type = request.POST.get('type')
        room.price = request.POST.get('price')
        room.hotel = request.POST.get('hotel')
        room.save()
        return redirect('/rooms')
    else:
        return render(request, 'insert_room.html')  

def insert_item(request):
    if request.method == 'POST':
        item = Item()
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.save()
        return redirect('/items')
    else:
        return render(request, 'insert_item.html')  

def insert_hotel(request):
    if request.method == 'POST':
        hotel = Hotel()
        hotel.name = request.POST.get('name')
        hotel.address = request.POST.get('address')
        hotel.save()
        return redirect('/hotels')
    else:
        return render(request, 'insert_hotel.html')   

def insert_customer(request):
    if request.method == 'POST':
        customer = Customer()
        customer.username = request.POST.get('username')
        customer.password = request.POST.get('password')
        customer.bill = request.POST.get('bill')
        customer.save()
        return redirect('/customers')
    else:
        return render(request, 'insert_customer.html')   

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

def edit_customer(request, pk):
    instance = Customer.objects.get(pk=pk)
    redirectUrl = "/customers"
    if request.method == 'POST':
        form = CustomerEditForm(request.POST)
        pk = request.session['pk']
        if pk == '':
            raise Http404
        if form.is_valid():
            instance.username=form.cleaned_data['username']
            instance.password=form.cleaned_data['password']
            instance.bill=form.cleaned_data['bill']
            instance.save(update_fields=['username', 'password', 'bill'])
            return HttpResponseRedirect(redirectUrl)
    else:
        if pk == '':
            raise Http404
        request.session['pk'] = pk
        form = CustomerEditForm({
            'username': instance.username,
            'password': instance.password,
            'bill': instance.bill,
        })
    return render(request, 'edit_customers.html', {'form': form.as_p()})