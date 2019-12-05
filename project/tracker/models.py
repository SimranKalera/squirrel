from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    x=models.FloatField(
            null=True,
            )
