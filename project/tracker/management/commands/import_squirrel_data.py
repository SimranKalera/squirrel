import csv
from django.db import IntegrityError
from django.core.management import BaseCommand
from tracker.models import Squirrel
import argparse

class Command(BaseCommand):
    help = 'Load a csv file into the database'
    
    def add_arguments(self,parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        print('Deleting all sightings..')
        Squirrel.objects.all().delete()
        print('Importing..');
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            next(reader,None)
            for row in reader:
                try: 
                    squirrel = Squirrel.objects.create(
                        longitude=row[0],
                        latitude=row[1],
                        unique_id=row[2],
                        shift=row[4],
                        date=row[5],
                        age=row[7],
                        primary_fur_color=row[8],
                        location=row[12],
                        specific_location=row[14],
                        running=(row[15]=='true'),
                        chasing=(row[16]=='true'),
                        climbing=(row[17]=='true'),
                        eating=(row[18]=='true'),
                        foraging=(row[19]=='true'),
                        other_activities=row[20],
                        kuks=(row[21]=='true'),
                        quaas=(row[22]=='true'),
                        moans=(row[23]=='true'),
                        tail_flags=(row[24]=='true'),
                        tail_twitches=(row[25]=='true'),
                        approaches=(row[26]=='true'),
                        indifferent=(row[27]=='true'),
                        runs_from=(row[28] == 'true'),
                    )
                    squirrel.save()
                except IntegrityError as e:
                    print('Skipping', row[2], 'due to integrity error')
