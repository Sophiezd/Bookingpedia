from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Room, Hotel, Reservation, Item, Transaction

admin.site.register(Customer)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Item)
admin.site.register(Transaction)