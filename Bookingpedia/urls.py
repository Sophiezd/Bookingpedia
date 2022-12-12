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
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from BookingpediaApp.views import CustomerListView, edit_customer, insert_hotel, HotelListView, reserved_hotels, \
    edit_hotel, RoomListView, edit_room, ReservationListView, edit_reservation, \
        ItemListView, edit_item, TransactionListView, edit_transaction, delete_customer, \
            delete_hotel, delete_reservation, delete_room, delete_item, delete_transaction, main_page , \
                insert_transaction, insert_reservation, insert_customer, insert_item, insert_room, pay_bill, \
                    HotelSearchListView, unreserved_hotels, CustomersSearchListView, sort_bill_cost_a, sort_bill_cost_d, \
                        HotelSearchAdminListView, room_start_date_asc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('userInfo.urls')),
    path('', main_page, name="home"),
    path('customers/', staff_member_required(CustomerListView.as_view(), login_url='login'), name="Customers"),
    path('customers/<int:pk>/edit/', edit_customer, name = 'editCustomers'),
    path('hotels/', staff_member_required(HotelListView.as_view(), login_url='login'), name="Hotels"),
    path('hotels/<int:pk>/edit/', edit_hotel, name = 'editHotels'),
    path('hotels/insert/',insert_hotel, name='insert_hotel'),
    path('customers/insert/',insert_customer, name='insert_customer'),
    path('items/insert/',insert_item, name='insert_item'),
    path('rooms/insert/',insert_room, name='insert_room'),
    path('reservations/insert/',insert_reservation, name='insert_reservation'),
    path('transactions/insert/',insert_transaction, name='insert_transaction'),
    path('rooms/', staff_member_required(RoomListView.as_view(), login_url='login'), name="Rooms"),
    path('rooms/<int:pk>/<int:roomNo>/edit/', edit_room, name = 'editRooms'),
    path('reservations/', staff_member_required(ReservationListView.as_view(), login_url='login'), name="Reservations"),
    path('reservations/<int:pk>/edit/', edit_reservation, name = 'editReservations'),
    path('items/', staff_member_required(ItemListView.as_view(), login_url='login'), name="Items"),
    path('items/<int:pk>/edit/', edit_item, name = 'editItems'),
    path('transactions/', staff_member_required(TransactionListView.as_view(), login_url='login'), name="Transactions"),
    path('transactions/<int:pk>/edit/', edit_transaction, name = 'editTransactions'),
    path('customers/<int:pk>/delete/', delete_customer, name = 'deleteCustomers'),
    path('hotels/<int:pk>/delete', delete_hotel, name = 'deleteHotels'),
    path('rooms/<int:pk>/<int:roomNo>/delete', delete_room, name = 'deleteRooms'),
    path('reservations/<int:pk>/delete', delete_reservation, name = 'deleteReservations'),
    path('items/<int:pk>/delete', delete_item, name = 'deleteItems'),
    path('transactions/<int:pk>/delete', delete_transaction, name = 'deleteTransactions'),
    path('reserved_hotels/', reserved_hotels, name='reserved_hotels'),
    path('unreserved_hotels/', unreserved_hotels, name='unreserved_hotels'),
    path('pay_bill', pay_bill, name='pay_bill'),
    path('cust_hot_search', login_required(HotelSearchListView.as_view(), login_url='login'), name='customer_hotel_search'),
    path('admin_search_cust/', CustomersSearchListView.as_view(), name='customer_name_search'),
    path('sort_customers_asc/', sort_bill_cost_a, name='sort_by_bill_a'),
    path('sort_customers_desc/', sort_bill_cost_d, name='sort_by_bill_d'),
    path('admin_search_hot/', HotelSearchAdminListView.as_view(), name='admin_hotel_search'),
    path('admin_sort_resv_date/', room_start_date_asc, name='admin_sorting_resv_date'),
]
