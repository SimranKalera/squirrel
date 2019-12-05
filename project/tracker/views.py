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
    squirrel= Squirrel.objects.get(id= unique_id)
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











# Create your views here.
