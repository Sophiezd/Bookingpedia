from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Customer, Room, Hotel, Reservation, Item, Transaction
from django.http import HttpResponseRedirect, Http404
from .forms import CustomerEditForm, HotelEditForm, RoomEditForm, ReservationEditForm, ItemEditForm, TransactionEditForm


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers.html'

class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels.html'

def insert_hotel(request):
    if request.method == 'POST':
        hotel = Hotel()
        hotel.name = request.POST.get('name')
        hotel.address = request.POST.get('address')
        hotel.save()
        return redirect('/hotels')
    else:
        return render(request, 'insert_hotel.html')   

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
    return render(request, 'edit.html', {'form': form.as_p()})

def edit_hotel(request, pk):
    instance = Hotel.objects.get(pk=pk)
    redirectUrl = "/hotels"
    if request.method == 'POST':
        form = HotelEditForm(request.POST)
        pk = request.session['pk']
        if pk == '':
            raise Http404
        if form.is_valid():
            instance.name=form.cleaned_data['name']
            instance.address=form.cleaned_data['address']
            instance.save(update_fields=['name', 'address'])
            return HttpResponseRedirect(redirectUrl)
    else:
        if pk == '':
            raise Http404
        request.session['pk'] = pk
        form = HotelEditForm({
            'name': instance.name,
            'address': instance.address,
        })
    return render(request, 'edit.html', {'form': form.as_p()})

def edit_item(request, pk):
    instance = Item.objects.get(pk=pk)
    redirectUrl = "/items"
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        pk = request.session['pk']
        if pk == '':
            raise Http404
        if form.is_valid():
            instance.name=form.cleaned_data['name']
            instance.price=form.cleaned_data['price']
            instance.save(update_fields=['name', 'price'])
            return HttpResponseRedirect(redirectUrl)
    else:
        if pk == '':
            raise Http404
        request.session['pk'] = pk
        form = ItemEditForm({
            'name': instance.name,
            'price': instance.price,
        })
    return render(request, 'edit.html', {'form': form.as_p()})

def edit_reservation(request, pk):
    instance = Reservation.objects.get(pk=pk)
    redirectUrl = "/reservations"
    if request.method == 'POST':
        form = ReservationEditForm(request.POST)
        pk = request.session['pk']
        if pk == '':
            raise Http404
        if form.is_valid():
            instance.start_date=form.cleaned_data['start_date']
            instance.end_date=form.cleaned_data['end_date']
            instance.room=form.cleaned_data['room']
            instance.customer=form.cleaned_data['customer']
            instance.save(update_fields=['start_date', 'end_date', 'room', 'customer'])
            return HttpResponseRedirect(redirectUrl)
    else:
        if pk == '':
            raise Http404
        request.session['pk'] = pk
        form = ReservationEditForm({
            'start_date': instance.start_date,
            'end_date': instance.end_date,
            'room': instance.room,
            'customer': instance.customer,
        })
    return render(request, 'edit.html', {'form': form.as_p()})

def edit_room(request, pk):
    instance = Room.objects.get(pk=pk)
    redirectUrl = "/rooms"
    if request.method == 'POST':
        form = RoomEditForm(request.POST)
        pk = request.session['pk']
        if pk == '':
            raise Http404
        if form.is_valid():
            instance.type=form.cleaned_data['type']
            instance.price=form.cleaned_data['price']
            instance.hotel=form.cleaned_data['hotel']
            instance.save(update_fields=['type', 'price', 'hotel'])
            return HttpResponseRedirect(redirectUrl)
    else:
        if pk == '':
            raise Http404
        request.session['pk'] = pk
        form = RoomEditForm({
            'type': instance.type,
            'price': instance.price,
            'hotel': instance.hotel,
        })
    return render(request, 'edit.html', {'form': form.as_p()})

def edit_transaction(request, pk):
    instance = Transaction.objects.get(pk=pk)
    redirectUrl = "/transactions"
    if request.method == 'POST':
        form = TransactionEditForm(request.POST)
        pk = request.session['pk']
        if pk == '':
            raise Http404
        if form.is_valid():
            instance.timestamp=form.cleaned_data['timestamp']
            instance.count=form.cleaned_data['count']
            instance.item=form.cleaned_data['item']
            instance.room=form.cleaned_data['room']
            instance.customer=form.cleaned_data['customer']
            instance.save(update_fields=['timestamp', 'count', 'item', 'room', 'customer'])
            return HttpResponseRedirect(redirectUrl)
    else:
        if pk == '':
            raise Http404
        request.session['pk'] = pk
        form = TransactionEditForm({
            'timestamp': instance.timestamp,
            'count': instance.count,
            'item': instance.item,
            'room': instance.room,
            'customer': instance.customer,
        })
    return render(request, 'edit.html', {'form': form.as_p()})