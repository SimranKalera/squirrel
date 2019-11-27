from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def all_squirrels(request):
    squirrels = Squirrel.objects.get(request)
    return Httpresponse("Hi")

# Create your views here.
