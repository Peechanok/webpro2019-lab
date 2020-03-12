from email.policy import default

from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
   
    name = models.CharField(max_length=50) 
    

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=20 )
    description = models.TextField()
    event_date = models.DateField( auto_now=False, auto_now_add=False, default = False )
    event_time = models.TimeField()
    location = models.CharField(max_length=200) 
    ticket_price = models.IntegerField(default=0)
    ticket_amount = models.IntegerField(default=0)
    usticket_amount = models.IntegerField( default=0)
    picture = models.ImageField(upload_to='media')
    POPPULAR = (
        ('Yes', 'Yes'),
        ('Not','Not'),
    )
    is_popular = models.CharField( max_length=20, choices=POPPULAR)
    
    

class Ticket(models.Model):
    
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_date = models.DateField( auto_now=False, auto_now_add=False)
