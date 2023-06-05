from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import sys

# Create your models here.

class Payment(models.Model):
    name = models.CharField(max_length=50, blank=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    receiver = models.CharField(max_length=50, blank=True)
    reference_number = models.PositiveIntegerField(blank=True, null=True)
    due_to = models.DateField(blank=True, null=True)
    account = models.CharField(max_length=75, null=True, blank=True)
    special_price_offsets = models.CharField(max_length=1000, blank=True)
     
    def __str__(self):
        return self.name



class EventForm(models.Model):
    name = models.CharField(max_length=50, blank=True)
    jason_content = models.CharField(max_length=4096)

    def __str__(self):
        return self.name
    


class Categories(models.Model):
    event_category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.event_category



class EventPoster(models.Model): 
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True, blank=True)
    phone = models.IntegerField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(null=True, default='images-2.jpg')
    category = models.ManyToManyField(Categories, blank=True)
    price_range = models.CharField(max_length=100, null=True, blank=True)
    poster = models.ForeignKey(EventPoster, null=True, on_delete=models.SET_NULL)
    participants = models.ManyToManyField(User, blank=True, related_name='participant')
    thank_you_text = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)
    payment = models.ForeignKey(
         Payment,
         null=True,
         blank=True,  
         on_delete=models.PROTECT
         )
    open_date = models.DateTimeField( 
        null=True, blank=True,             
        default=timezone.datetime(2018, 1, 1)
        )
    close_date = models.DateTimeField()


    
    def __str__(self):
        return self.name
    
    

    def is_yet_open_for_registration(self):
        return not self.open_date or self.open_date < timezone.now()

    def is_past(self):
        if timezone.now() > self.close_date:
            return True
        return False

    def is_full(self):
        count = User.objects.filter(event__id=self.id).count()
        capacity = self.capacity if self.capacity is not None else sys.maxsize
        if capacity <= count:
            return True
        return False

    def is_hide(self):
        return self.hide or self.open_date < timezone.now()
        


class Submission(models.Model):
    participants = models.ManyToManyField(User, blank=True, related_name='attendee')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.event) + '---' + str(self.participants)
    

class Applauders(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(null=True)



class Volunteers(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(null=True)

class SeatWarmers(models.Model):   
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    #age = models.PositiveIntegerField(null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(null=True)