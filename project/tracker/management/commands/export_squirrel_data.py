from django.core.management.base import BaseCommand

import csv
  
from tracker.models import Squirrel
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        dict_export = {}
        s = Squirrel.objects.all()
        with open(options['csv_file'],"w") as fp:
            for i in s:
                dict_export['longitude'] = i.longitude
                dict_export['latitude'] = i.latitude
                dict_export['shift'] = i.shift
                dict_export['date'] = i.date
                dict_export['unique id'] = i.unique_id
                dict_export['age'] = i.age
                dict_export['Primary fur Color'] = i.primary_fur_color
                dict_export['Location'] = i.location
                dict_export['Specific Location'] = i.specific_location
                dict_export['Running'] = i.running
                dict_export['Chasing'] = i.chasing
                dict_export['Climbing'] = i.climbing
                dict_export['Eating'] = i.eating
                dict_export['Foraging'] = i.foraging
                dict_export['Other Activities'] = i.other_activities
                dict_export['Kuks'] = i.kuks
                dict_export['Quaas'] = i.quaas
                dict_export['Moans'] = i.moans
                dict_export['Tail Flags'] = i.tail_flags
                dict_export['Tail Twitches'] = i.tail_twitches
                dict_export['Approaches'] = i.approaches
                dict_export['Indifferent'] = i.indifferent
                dict_export['Runs from'] = i.runs_from
               
                write = csv.DictWriter(fp,delimiter=",",fieldnames=dict_export.keys())
                write.writeheader()
                write.writerow(dict_export)
