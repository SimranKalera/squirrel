from django.core.management.base import BaseCommand
import os, csv

class Command(BaseCommand):
    help = 'Import data from 2018 census file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Indicates the file path of the squirrel data file')

    def handle(self, *args):
        file_path = args[0]
        if not os.path.exists(file_path):
            raise CommandError("%s doesnt exist"%file_path)

        with open (file_path, 'rb') as csvFile:
            reader = csv.reader(csvFile, delimitirer=',')
