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
                    latitude = row[1][1],
                    longitude = row[1][0],
                    unique_id = row[1][2],
                    shift = row[1][4],
                    date = row[1][5],
                    age = row[1][7],
                    primary_fur_color = row[1][8],
                    location = row[1][12],
                    specific_location = row[1][14],
                    quaas = row[1][22],
                    moans = row[1][23],
                    tail_flags = row[1][24],
                    tail_twitches = row[1][25],
                    approaches = row[1][26],
                    indifferent = row[1][27],
                    runs_from = row[1][28],
                    running = row[1][15],
                    chasing = row[1][16],
                    climbing = row[1][17],
                    eating = row[1][18],
                    foraging = row[1][19],
                    other_activities = row[1][20],
                    kuks = row[1][21],
                    )
               for row in data.iterrows()
               ]
        Squirrel.objects.bulk_create(squirrels)
            
