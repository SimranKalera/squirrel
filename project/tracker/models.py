from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    date = models.DateField(
            help_text=_('Sighting date of squirrel'),
            )
# Create your models here.
