from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views.generic import ListView
from .models import Customer, Room, Hotel, Reservation, Item, Transaction
from django.http import HttpResponseRedirect, Http404
from .forms import CustomerEditForm, HotelEditForm, RoomEditForm, ReservationEditForm, ItemEditForm, TransactionEditForm, PayBillForm
from django.db.models import Q
from django.utils import timezone

from .sql_run import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

class CustomerListView(ListView):
    model = Customer
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_details'] = get_customer_details()
        return context
    template_name = 'customers.html'

class HotelListView(ListView):
    model = Hotel
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel_details'] = get_hotel_details()
        return context
    template_name = 'hotels.html'

@staff_member_required(login_url='login')
def insert_transaction(request):
    if request.method == 'POST':
        transaction = Transaction()
        transaction.timestamp = request.POST.get('timestamp')
        transaction.count = request.POST.get('count')
        item_pk = request.POST.get('item')
        customer_pk = request.POST.get('customer')
        [hotel_pk, room] = request.POST.get('room').split('|')
        transaction.item = Item.objects.get(pk=item_pk)
        transaction.customer = Customer.objects.get(pk=customer_pk)
        match_hotel = Hotel.objects.get(pk=hotel_pk)
        transaction.room = Room.objects.get(
            Q(hotel=match_hotel),
            Q(number=room)
        )
        transaction.save()
        return redirect('/transactions')
    else:
        rooms = Room.objects.all()
        customers = Customer.objects.all()
        items = Item.objects.all()
        return render(request, 'insert_transaction.html', {'rooms': rooms, 'customers': customers, 'items': items})  

@staff_member_required(login_url='login')
def insert_reservation(request):
    if request.method == 'POST':
        [hotel_pk, room] = request.POST.get('room').split('|')
        reservation = Reservation()
        reservation.start_date = request.POST.get('start_date')
        reservation.end_date = request.POST.get('end_date')        
        customer_pk = request.POST.get('customer')
        reservation.customer = Customer.objects.get(pk=customer_pk)
        match_hotel = Hotel.objects.get(pk=hotel_pk)
        reservation.room = Room.objects.get(
            Q(hotel=match_hotel),
            Q(number=room)
        )
        reservation.save()
        return redirect('/reservations')
    else:
        rooms = Room.objects.all()
        customers = Customer.objects.all()
        return render(request, 'insert_reservation.html', {'rooms': rooms, 'customers': customers})  

@staff_member_required(login_url='login')
def insert_room(request):
    if request.method == 'POST':
        room = Room()
        room.number = request.POST.get('roomNo')
        room.type = request.POST.get('type')
        room.price = request.POST.get('price')
        hotel_pk = request.POST.get('hotel')
        room.hotel = Hotel.objects.get(pk=hotel_pk)
        try:
            room.save()
            return redirect('/rooms')
        except IntegrityError as e:
            messages.error(request, ('That hotel already has a Room ' + str(room.number) + '!'))
            hotels = Hotel.objects.all()
            return render(request, 'insert_room.html', {'hotels': hotels})  
        
    else:
        hotels = Hotel.objects.all()
        return render(request, 'insert_room.html', {'hotels': hotels})  

@staff_member_required(login_url='login')
def insert_item(request):
    if request.method == 'POST':
        item = Item()
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.save()
        return redirect('/items')
    else:
        return render(request, 'insert_item.html')  

@staff_member_required(login_url='login')
def insert_hotel(request):
    if request.method == 'POST':
        hotel = Hotel()
        hotel.name = request.POST.get('name')
        hotel.address = request.POST.get('address')
        hotel.save()
        return redirect('/hotels')
    else:
        return render(request, 'insert_hotel.html')   

@staff_member_required(login_url='login')
def insert_customer(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        b = request.POST.get('bill')
        Customer.objects.create_user(username=u, password=p, bill=b)
        return redirect('/customers')
    else:
        return render(request, 'insert_customer.html')   

class RoomListView(ListView):
    model = Room    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_details'] = get_room_details()
        return context
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

@staff_member_required
def reserved_hotels(request):
    template_name = 'reserved_hotels.html'
    context = {'reserved_hotels': get_reserved_rooms()}     
    return render(request, template_name, context)

def unreserved_hotels(request):
    template_name = 'unreserved_hotels.html'
    context = {'unreserved_hotels': get_unreserved_rooms()}     
    return render(request, template_name, context)

@staff_member_required(login_url='login')
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
            instance.bill=form.cleaned_data['bill']
            password=form.cleaned_data['password']
            if (password):
                instance.set_password(password)
                instance.save(update_fields=['username', 'password', 'bill'])
            else:
                instance.save(update_fields=['username', 'bill'])
            return HttpResponseRedirect(redirectUrl)
    else:
        if pk == '':
            raise Http404
        request.session['pk'] = pk
        form = CustomerEditForm({
            'username': instance.username,
            'bill': instance.bill,
        })
    return render(request, 'edit.html', {'form': form.as_p()})

@staff_member_required(login_url='login')
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

@staff_member_required(login_url='login')
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

@staff_member_required(login_url='login')
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

@staff_member_required(login_url='login')
def edit_room(request, pk, roomNo):
    match_hotel = Hotel.objects.get(pk=pk)
    instance = Room.objects.get(
        Q(hotel=match_hotel),
        Q(number=roomNo)
    )
    redirectUrl = "/rooms"
    if request.method == 'POST':
        form = RoomEditForm(request.POST)
        pk = request.session['pk']
        if pk == '':
            raise Http404
        if form.is_valid():
            instance.number=form.cleaned_data['number']
            instance.type=form.cleaned_data['type']
            instance.price=form.cleaned_data['price']
            instance.hotel=form.cleaned_data['hotel']
            try:
                instance.save(update_fields=['number', 'type', 'price', 'hotel'])
                return HttpResponseRedirect(redirectUrl)
            except IntegrityError as e:
                form = RoomEditForm({
                    'number': instance.number,
                    'type': instance.type,
                    'price': instance.price,
                    'hotel': instance.hotel,
                })
                messages.error(request, ('That hotel alread has a Room ' + str(instance.number) + '!'))
                return render(request, 'edit.html', {'form': form.as_p()})
    else:
        if pk == '':
            raise Http404
        request.session['pk'] = pk
        form = RoomEditForm({
            'number': instance.number,
            'type': instance.type,
            'price': instance.price,
            'hotel': instance.hotel,
        })
    return render(request, 'edit.html', {'form': form.as_p()})

@staff_member_required(login_url='login')
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

@staff_member_required(login_url='login')
def delete_customer(request, pk):
    customer_del = Customer.objects.get(pk=pk)
    customer_del.delete()
    return HttpResponseRedirect("/customers")

def main_page(request):
    user = request.user
    if user.is_superuser:
        return render(request, 'main.html')
    else:
        return redirect('login')
    

@staff_member_required(login_url='login')
def delete_hotel(request, pk):
    hotel_del = Hotel.objects.get(pk=pk)
    hotel_del.delete()
    return HttpResponseRedirect("/hotels")

@staff_member_required(login_url='login')
def delete_reservation(request, pk):
    reservation_del = Reservation.objects.get(pk=pk)
    reservation_del.delete()
    return HttpResponseRedirect("/reservations")

@staff_member_required(login_url='login')
def delete_room(request, pk, roomNo):
    match_hotel = Hotel.objects.get(pk=pk)
    room_del = Room.objects.get(
        Q(hotel=match_hotel),
        Q(number=roomNo)
    )
    room_del.delete()
    return HttpResponseRedirect("/rooms")

@staff_member_required(login_url='login')
def delete_transaction(request, pk):
    transaction_del = Transaction.objects.get(pk=pk)
    transaction_del.delete()
    return HttpResponseRedirect("/transactions")

@staff_member_required(login_url='login')
def delete_item(request, pk):
    item_del = Item.objects.get(pk=pk)
    item_del.delete()
    return HttpResponseRedirect("/items")

@login_required(login_url='login')
def pay_bill(request):
    instance = request.user
    if request.method == 'POST':
        form = PayBillForm(request.POST)
        if form.is_valid():
            instance.bill-=form.cleaned_data['payment']
            if (instance.bill < 0):
                instance.bill = 0
            instance.save(update_fields=['bill',])
            return redirect('home')
    else:
        form = PayBillForm({
            'payment': instance.bill,
        })
    return render(request, 'pay_bill.html', {'form': form.as_p()})

class CustHotelListView(ListView):
    model = Hotel
    template_name = 'cust_hotel_search.html'

class HotelSearchListView(ListView):
    model = Hotel
    template_name = 'cust_hotel_browse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotnames'] = Hotel.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = get_hotel_name(query)
        return object_list


class CustomersSearchListView(ListView):
    model = Customer
    template_name = 'admin_search_cust.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custnames'] = Customer.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = get_customer_name(query)
        return object_list

    
@staff_member_required(login_url='login')
def sort_bill_cost_a(request):
    template_name = 'sort_customers.html'
    context = {'sort_customers_a': sort_bill_cust_a()}     
    return render(request, template_name, context)

@staff_member_required(login_url='login')
def sort_bill_cost_d(request):
    template_name = 'sort_customers.html'
    context = {'sort_customers_d': sort_bill_cust_d()}     
    return render(request, template_name, context)

@staff_member_required(login_url='login')
def room_start_date_asc(request):
    template_name = 'admin_sort_resv_date.html'
    context = {'sort_resv_date': sort_start_date_acs()}    
    print(context) 
    return render(request, template_name, context)


class HotelSearchAdminListView(ListView):
    model = Hotel
    template_name = 'admin_search_hot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotnames'] = Hotel.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = get_hotel_name(query)
        return object_list

@login_required(login_url='login')
def cust_room_list(request, pk):
    match_hotel = Hotel.objects.get(pk=pk)
    instance = get_hotel_rooms(match_hotel.pk)
    return render(request, 'cust_room_search.html', {'object_list': instance})

@login_required(login_url='login')
def cust_room_res(request, pk):
    match_hotel = Hotel.objects.get(pk=pk)
    max = request.GET.get("price_max")
    min = request.GET.get("price_min")
    if max and min:
        print('call 1')
        instance = get_hotel_rooms_between(match_hotel.pk, max, min)
    elif max:
        print('call 2')
        instance = get_hotel_rooms_max(match_hotel.pk, max)
    elif min:
        print('call 3')
        instance = get_hotel_rooms_min(match_hotel.pk, min)
    else:
        print('call 4')
        instance = get_hotel_rooms(match_hotel.pk)
    return render(request, 'cust_room_browse.html', {'object_list': instance})

@login_required(login_url='login')
def make_reservation(request, hpk, rpk):
    if request.method == 'POST':
        reservation = Reservation()
        reservation.start_date = request.POST.get('start_date')
        reservation.end_date = request.POST.get('end_date')        
        reservation.customer = request.user
        match_hotel = Hotel.objects.get(pk=hpk)
        reservation.room = Room.objects.get(
            Q(hotel=match_hotel),
            Q(number=rpk)
        )
        reservation.customer.bill += reservation.room.price
        reservation.save()
        reservation.customer.save()
        return redirect('my_reservations')
    else:
        return render(request, 'reserve_room.html', {})

@login_required(login_url='login')
def my_res(request):
    res_list = get_reservations(request.user.id)
    return render(request, 'your_reserv.html', {'object_list': res_list})

@login_required(login_url='login')
def buy_item(request, pk):
    if request.method == 'POST':
        transaction = Transaction()
        transaction.timestamp = timezone.now()
        transaction.count = request.POST.get('count')
        item_id = request.POST.get('item')
        transaction.item = Item.objects.get(pk=item_id)
        customer = request.user
        transaction.customer = customer
        reserv = Reservation.objects.get(pk=pk)
        transaction.room = reserv.room
        customer.bill += round(float(transaction.item.price) * float(transaction.count))
        transaction.save()
        customer.save()
        return redirect('home')
    else:
        reserv = Reservation.objects.get(pk=pk)
        items = Item.objects.all()
        return render(request, 'order_item.html', {'object_list': items, 'reservation': reserv})
class ItemsSearchListView(ListView):
    model = Item
    template_name = 'admin_search_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itemnames'] = Item.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = get_item_name(query)
        return object_list

class ItemsSearchListView2(ListView):
    model = Item
    template_name = 'admin_search_item2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itemnames'] = Item.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = get_item_price(query)
        return object_list

class TransactionSearchListView(ListView):
    model = Transaction
    template_name = 'admin_search_transaction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transnames'] = Transaction.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = get_transaction_item(query)
        return object_list

class TransactionSearchListView2(ListView):
    model = Transaction
    template_name = 'admin_search_transaction2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transnames'] = Transaction.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = get_transaction_customer(query)
        return object_list