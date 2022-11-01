from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    bill = models.FloatField(default=0)

    def __str__(self):
        return self.username

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.IntegerField(default=0)
    type = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    hotel = models.ForeignKey(Hotel, related_name='Rooms', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hotel) + ", Room: " + str(self.number)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['number', 'hotel'], name='unique_number_hotel_combination'
            )
        ]

class Reservation(models.Model):
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    room = models.ForeignKey(Room, related_name='Reservations', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='Reservations', on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.FloatField(default=0)
    item = models.ForeignKey(Item, related_name='Transactions', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='Transactions', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='Transactions', on_delete=models.CASCADE)