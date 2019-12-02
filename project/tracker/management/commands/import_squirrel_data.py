from django.core.management.base import BaseCommand
import os, csv, sys
import pandas as pd
from tracker.models import Squirrel

class Command(BaseCommand):
    help = 'Import data from 2018 census file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Indicates the file path of the squirrel data file')

    def handle(self, *args, **kwargs):
        file_path = sys.argv[0]
        if not os.path.exists(file_path):
            raise CommandError("%s doesnt exist"%file_path)
        
        data = pd.read_csv(file_path, delimiter=',', error_bad_lines=False)
        squirrels = [
                Squirrel(
                    latitude = tuple(pd.DataFrame(row[1]).iloc[1]),
                    longitude = tuple(pd.DataFrame(row[1]).iloc[0]),
                    unique_id = tuple(pd.DataFrame(row[1]).iloc[2]),
                    shift = tuple(pd.DataFrame(row[1]).iloc[4]),
                    date = tuple(pd.DataFrame(row[1]).iloc[5]),
                    age = tuple(pd.DataFrame(row[1]).iloc[7]),
                    primary_fur_color = tuple(pd.DataFrame(row[1]).iloc[8]),
                    location = tuple(pd.DataFrame(row[1]).iloc[12]),
                    specific_location = tuple(pd.DataFrame(row[1]).iloc[14]),
                    quaas = tuple(pd.DataFrame(row[1]).iloc[22]),
                    moans = tuple(pd.DataFrame(row[1]).iloc[23]),
                    tail_flags = tuple(pd.DataFrame(row[1]).iloc[24]),
                    tail_twitches = tuple(pd.DataFrame(row[1]).iloc[25]),
                    aeproaches = tuple(pd.DataFrame(row[1]).iloc[26]),
                    indifferent = tuple(pd.DataFrame(row[1]).iloc[27]),
                    runs_from = tuple(pd.DataFrame(row[1]).iloc[28]),
                    running = tuple(pd.DataFrame(row[1]).iloc[15]),
                    chasing = tuple(pd.DataFrame(row[1]).iloc[16]),
                    climbing = tuple(pd.DataFrame(row[1]).iloc[17]),
                    eating = tuple(pd.DataFrame(row[1]).iloc[18]),
                    foraging = tuple(pd.DataFrame(row[1]).iloc[19]),
                    other_activities = tuple(pd.DataFrame(row[1]).iloc[20]),
                    kuks = tuple(pd.DataFrame(row[1]).iloc[21]),
                    )
               for row in data.iterrows()
               ]
        Squirrel.objects.bulk_create(squirrels)
            
