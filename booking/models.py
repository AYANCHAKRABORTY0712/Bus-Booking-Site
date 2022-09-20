from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

class USER(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    username = models.TextField(max_length=20,primary_key=True)
    password = models.TextField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.name
        
class BUS(models.Model):
    agency=models.CharField(max_length=50,default='')
    bustype=models.CharField(max_length=20,default='')
    bus_ID=models.CharField(max_length=20,default='',primary_key=True)
    route=models.CharField(max_length=10,null=True)
    From=models.CharField(max_length=100,default='')
    To=models.CharField(max_length=100,default='')
    BoardPoint=models.CharField(max_length=50,default='',null=True)
    DropPoint=models.CharField(max_length=50,default='')
    AvS=models.IntegerField(default=45)
    seats={
        "seniors":4,
        "ladies":4,
        "PwD":2,
        "transgender":1,
        "general":34
    }
    seatno=['S'+str(i) for i in range(1,46)]
    BkS=models.IntegerField(default=0)
    Date=models.DateField(default='')
    BTime=models.TimeField(default='')
    DTime=models.TimeField(default='')
    TravelTime=models.CharField(max_length=10, default='')
    Rate=models.FloatField(default=50.00)

    def _str_(self):
        return self.bus_ID

class Booking(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Bus_ID=models.CharField(max_length=20,default='')
    Departure_Date=models.CharField(max_length=20,default='')
    JTime=models.CharField(max_length=20,default='')
    Pickup=models.CharField(max_length=50,default='')
    Destination=models.CharField(max_length=50,default='')
    seniors=models.IntegerField()
    ladies=models.IntegerField()
    PwD=models.IntegerField()
    transgender=models.IntegerField()
    general=models.IntegerField()
    charges=models.IntegerField()

    def _str_(self):
        return self.Bus_ID

class Contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Message=models.TextField(max_length=200)

    def _str_(self):
        return self.Email




    