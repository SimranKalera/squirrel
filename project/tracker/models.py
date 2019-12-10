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
            primary_key=True,
            )
    
    AM = 'am'
    PM = 'pm'
    ADULT = 'adult'
    JUVENILE = 'juvenile'
    GRAY = 'gray'
    CINNAMON = 'cinnamon'
    BLACK = 'black'
    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    OTHER ='other'

    
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
            (OTHER, 'Other'),
            )
    
    shift = models.CharField(
            max_length =5,
            choices = SHIFT_CHOICES,
            help_text=_('Sighting occurred in the morning or late afternoon'),
            default = OTHER,
            )

    date = models.CharField(
            max_length =8,
         
            help_text=_('Concatenation of the sighting session day and month'),
            )
    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (OTHER, 'Other'),
            )
    
    age= models.CharField(
            max_length =50,
            choices = AGE_CHOICES,
            help_text=_('Value is either Adult or Juvenile'),
            default = OTHER,
            )
    COLOR_CHOICES = (
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
            (BLACK, 'Black'),
            (OTHER, 'Other'),
            )
    primary_fur_color= models.CharField(
            max_length =50,
            choices= COLOR_CHOICES,
            help_text=_('Value is either "Gray," "Cinnamon" or "Black."'),
            default =OTHER,
            )


    
    
    LOCATION_CHOICES = (
            (GROUND_PLANE , 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            (OTHER, 'Other'),
            )
    location = models.CharField(
            max_length=50,
            choices=LOCATION_CHOICES,
            default=OTHER,
            help_text=_('Location of where the squirrel was when first sighted'),
            )
    specific_location = models.CharField(
            max_length=300,
            help_text=_('Additional commentary on the squirrel location'),
            )
    quaas = models.BooleanField(
            default=False,
            help_text=_('Whether the squirrel was heard quaaing'),
            )
    moans = models.BooleanField(
            default=False,
            help_text=_('Whether the squirrel was heard moaning'),
            )
    tail_flags = models.BooleanField(
            help_text=_('Whether the squirrel was seen flagging its tail'),
            default=False,
            )
    tail_twitches = models.BooleanField(
            help_text=_('Whether the squirrel was seen twitching its tail'),
            default=False,
            )
    approaches = models.BooleanField(
            help_text=_('Whether the squirrel was seen approaching human, seeking foodl'),
            default=False,
            )
    indifferent = models.BooleanField(
            help_text=_('Whether the Squirrel was indifferent to human presence'),
            default=False,
            )
    runs_from = models.BooleanField(
            help_text=_('Whether the Squirrel was seen running from humans, seeing them as a threat'),
            default=False,
            )

    running = models.BooleanField(
            help_text=_('Whether squirrel was seen running'),
            default=False,
            )
    chasing = models.BooleanField(
            help_text=_('Whether squirrel was seen chasing another squirrel.'),
            default=False,
            )
    climbing = models.BooleanField(
            help_text=_('Whether Squirrel was seen climbing a tree or other environmental landmark.'),
            default=False,
            )
    eating = models.BooleanField(
            help_text=_('Whether squirrel was seen eating'),
            default=False,
            )
    foraging = models.BooleanField(
            help_text=_('Whether squirrel was seen foraging for food'),
            default=False,
            )
    other_activities = models.CharField(
            max_length=200,
            help_text=_('Whether squirrel was seen engaged in any other activity'),
            )
    kuks = models.BooleanField(
            help_text=_('Whether squirrel was heard kukking'),
            default=False,
            )
