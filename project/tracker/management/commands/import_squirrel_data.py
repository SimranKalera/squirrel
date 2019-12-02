from django.core.management.base import BaseCommand
import os, csv
import pandas as pd
from tracker.models import Squirrel

class Command(BaseCommand):
    help = 'Import data from 2018 census file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Indicates the file path of the squirrel data file')

    def import_data(self, *args):
        file_path = args[0]
        if not os.path.exists(file_path):
            raise CommandError("%s doesnt exist"%file_path)
        
        data = pd.read_csv(file_path)
        squirrels = [
                Squirrel(
                    latitude = data.ix[row]['Y']
                    longitude = data.ix[row]['X']
                    unique_id = data.ix[row]['Unique Squirrel ID']
                    shift = data.ix[row]['Shift']
                    date = data.ix[row]['Date']
                    age = data.ix[row]['Age']
                    primary_fur_color = data.ix[row]['Primary Fur Color']
                    location = data.ix[row]['Location']
                    specific_location = data.ix[row]['Specific Location']
                    quaas = data.ix[row]['Quaas']
                    moans = data.ix[row]['Moans']
                    tail_flags = data.ix[row]['Tail flags']
                    tail_twitches = data.ix[row]['Tail twitches']
                    approaches = data.ix[row]['Approaches']
                    indifferent = data.ix[row]['Indifferent']
                    runs_from = data.ix[row]['Runs from']
                    running = data.ix[row]['Running']
                    chasing = data.ix[row]['Chasing']
                    climbing = data.ix[row]['Climbing']
                    eating = data.ix[row]['Eating']
                    foraging = data.ix[row]['Foraging']
                    other_activities = data.ix[row]['Other Activites']]
                    kuks = data.ix[row]['Kuks']
                    )
               for row in data
               ]
        Squirrel.objects.bulk_create(squirrels)
            
