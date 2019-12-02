from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField(
            help_text=_('Latitude coordinate for squirrel sighting point'),
            )
    longitude = models.FloatField(
            help_text=_('Longitude coordinate for squirrel sighting point'),
            )
    unique_id = models.CharField(
            max_length =50, 
            help_text=_('Identification tag for each squirrel sighting'),
            )
    
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
            )
    
    shift = models.CharField(
            max_length =5,
            choices = SHIFT_CHOICES,
            help_text=_('Sighting occurred in the morning or late afternoon'),
            )

    date = models.CharField(
            max_length =8,
            help_text=_('Concatenation of the sighting session day and month'),
            )
    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            )
    
    age= models.CharField(
            max_length =50,
            choices = AGE_CHOICES,
            help_text=_('Value is either Adult or Juvenile'),
            )
    COLOR_CHOICES = (
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
            (BLACK, 'Black'),
            )
    primary_fur_color= models.CharField(
            max_length =50,
            choices= COLOR_CHOICES,
            help_text=_('Value is either "Gray," "Cinnamon" or "Black."'),
            )
    LOCATION_CHOICES = (
            (GROUND_PLANE , 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            )
    location = models.CharField(
            max_length=50,
            choices=LOCATION_CHOICES,
            help_text=_('Location of where the squirrel was when first sighted'),
            )
    specific_location = models.CharField(
            max_length=300,
            help_text=_('Additional commentary on the squirrel location'),
            )
    running = models.BooleanField(
            help_text=_('Whether squirrel was seen running'),
            )
    chasing = models.BooleanField(
            help_text=_('Whether squirrel was seen chasing another squirrel.'),
            )
    climbing = models.BooleanField(
            help_text=_('Whether Squirrel was seen climbing a tree or other environmental landmark.'),
            )
    eating = models.BooleanField(
            help_text=_('Whether squirrel was seen eating'),
            )
    foraging = models.BooleanField(
            help_text=_('Whether squirrel was seen foraging for food'),
            )
    other_activities = models.CharField(
            max_length=200,
            help_text=_('Whether squirrel was seen engaged in any other activity'),
            )
    kuks = models.BooleanField(
            help_text=_('Whether squirrel was heard kukking'),
            )
  



# Create your models here.
