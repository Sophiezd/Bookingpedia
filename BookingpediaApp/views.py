from django.shortcuts import render
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