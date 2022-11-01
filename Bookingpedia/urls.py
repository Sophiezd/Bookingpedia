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
from BookingpediaApp.views import CustomerListView, insert_reservation, insert_room, insert_transaction, insert_item, insert_customer, edit_customer, HotelListView, RoomListView, ReservationListView, ItemListView, TransactionListView, insert_hotel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', CustomerListView.as_view(), name="Customers"),
    path('customers/<int:pk>/edit/', edit_customer, name = 'editCustomers'),
    path('hotels/', HotelListView.as_view(), name="Hotels"),
    path('hotels/insert/',insert_hotel, name='insert_hotel'),
    path('customers/insert/',insert_customer, name='insert_customer'),
    path('rooms/', RoomListView.as_view(), name="Rooms"),
    path('rooms/insert/',insert_room, name='insert_room'),
    path('items/insert/',insert_item, name='insert_item'),
    path('transactions/insert/',insert_transaction, name='insert_transaction'),
    path('reservations/', ReservationListView.as_view(), name="Reservations"),
    path('reservations/insert/',insert_reservation, name='insert_reservation'),
    path('items/', ItemListView.as_view(), name="Items"),
    path('transactions/', TransactionListView.as_view(), name="Transactions"),
]
