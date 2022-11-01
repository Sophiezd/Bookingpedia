from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    bill = models.FloatField(default=0)

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Room(models.Model):
    type = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    hotel = models.ForeignKey(Hotel, related_name='Rooms', on_delete=models.CASCADE)

class Reservation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, related_name='Reservations', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='Reservations', on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)

class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.FloatField(default=0)
    Item = models.ForeignKey(Item, related_name='Transactions', on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, related_name='Transactions', on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, related_name='Transactions', on_delete=models.CASCADE)