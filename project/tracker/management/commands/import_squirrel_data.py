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

        with open(file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Squirrel.objects.get_or_create(
                        latitude = row[1]
                        longitude = row[0]
                        unique_id = row[2]
                        shift = row[4]
                        date = row[5]
                        age = row[7]
                        primary_fur_color = row[8]
                        location = row[12]
                        specific_location = row[14]
                        quaas = row[22]
                        moans = row[23]
                        tail_flags = row[24]
                        tail_twitches = row[25]
                        approaches = row[26]
                        indifferent = row[27]
                        runs_from = row[28]
                        running = row[15]
                        chasing = row[16]
                        climbing = row[17]
                        eating = row[18]
                        foraging = row[19]
                        other_activities = row[20]
                        kuks = row[21]
                        )
            created.save()
