"""Bookingpedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from BookingpediaApp.views import CustomerListView, edit_customer, insert_hotel, HotelListView, reserved_hotels, \
    edit_hotel, RoomListView, edit_room, ReservationListView, edit_reservation, \
        ItemListView, edit_item, TransactionListView, edit_transaction, delete_customer, \
            delete_hotel, delete_reservation, delete_room, delete_item, delete_transaction, main_page , \
                insert_transaction, insert_reservation, insert_customer, insert_item, insert_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name="home"),
    path('customers/', CustomerListView.as_view(), name="Customers"),
    path('customers/<int:pk>/edit/', edit_customer, name = 'editCustomers'),
    path('hotels/', HotelListView.as_view(), name="Hotels"),
    path('hotels/<int:pk>/edit/', edit_hotel, name = 'editHotels'),
    path('hotels/insert/',insert_hotel, name='insert_hotel'),
    path('customers/insert/',insert_customer, name='insert_customer'),
    path('items/insert/',insert_item, name='insert_item'),
    path('rooms/insert/',insert_room, name='insert_room'),
    path('reservations/insert/',insert_reservation, name='insert_reservation'),
    path('transactions/insert/',insert_transaction, name='insert_transaction'),
    path('rooms/', RoomListView.as_view(), name="Rooms"),
    path('rooms/<int:pk>/<int:roomNo>/edit/', edit_room, name = 'editRooms'),
    path('reservations/', ReservationListView.as_view(), name="Reservations"),
    path('reservations/<int:pk>/edit/', edit_reservation, name = 'editReservations'),
    path('items/', ItemListView.as_view(), name="Items"),
    path('items/<int:pk>/edit/', edit_item, name = 'editItems'),
    path('transactions/', TransactionListView.as_view(), name="Transactions"),
    path('transactions/<int:pk>/edit/', edit_transaction, name = 'editTransactions'),
    path('customers/<int:pk>/delete/', delete_customer, name = 'deleteCustomers'),
    path('hotels/<int:pk>/delete', delete_hotel, name = 'deleteHotels'),
    path('rooms/<int:pk>/<int:roomNo>/delete', delete_room, name = 'deleteRooms'),
    path('reservations/<int:pk>/delete', delete_reservation, name = 'deleteReservations'),
    path('items/<int:pk>/delete', delete_item, name = 'deleteItems'),
    path('transactions/<int:pk>/delete', delete_transaction, name = 'deleteTransactions'),
    path('reserved_hotels/', reserved_hotels, name='reserved_hotels')
]
