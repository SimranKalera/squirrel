from django.forms import ModelForm
from .models import Squirrel
from django import forms

class SquirrelForm(ModelForm):
    specific_location = forms.CharField(required=False)
    other_activities = forms.CharField(required=False)
    class Meta:
        model = Squirrel
        fields = '__all__'
