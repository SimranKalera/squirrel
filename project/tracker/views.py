from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel


def map(request):
    sightings= Squirrel.objects.all()[:100]
    context={
            'sightings':sightings,
        }
    return render(request, 'tracker/map.html',context)


def sightings(request):
    squirrels= Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }
    return render(request, 'tracker/sightings.html', context)

def update(request, unique_id):
<<<<<<< HEAD
    squirrel= Squirrel.objects.get(id= unique_id)
=======
    squirrel= Squirrel.objects.get(unique_id = unique_id)
>>>>>>> 6adfa0b1aaf26fad6fe7a25368b7e0d32f7e3782
    if request.method == 'POST':
        form = SquirrelForm (request.POST, instance = squirrel)

        if form.is_valid():
            form.save()
            return redirect(f'/tracker/{unique_id}')

    else:
        form = SquirrelForm()
    context = {
            'form': form,
            }
    return render(request, 'tracker/update.html', context)

<<<<<<< HEAD
=======
def create(request):
    if request.method=='POST':
        form = SquirrelForm(request.POST)
        if form.isvalid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()
    context={
            'form':form,
            }
    return render(request, 'tracker/update.html' context)

def view_stats(request):
    am=0
    pm=0
    running=0
    chasing=0
    eating=0
    climbing=0
    squirrels = Squirrel.objects.all()
    for s in squirrels:
        if s.shift=='AM':
            am += 1
        elif s.shift=='PM':
            pm += 1
        if s.running==True:
            running += 1
        if s.chasing==True:
            chasing += 1
        if s.eating==True:
            eating += 1
        if s.climbing==True:
            climbing += 1
    context ={
            'Shift - AM Count':am,
            'Shift - PM Count':pm,
            'Running Count':running,
            'Chasing Count':chasing,
            'Eating Count':eating,
            'Climbing Count': climbing,
            }
    return render(request, 'tracker/stats.html', context)
>>>>>>> 6adfa0b1aaf26fad6fe7a25368b7e0d32f7e3782










# Create your views here.
