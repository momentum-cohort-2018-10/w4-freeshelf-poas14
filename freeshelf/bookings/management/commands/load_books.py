from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from bookings.models import Book
from django.core.files import File

import pdb

def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)

class Command(BaseCommand):
    help = "My shiny new management command by peter."

    def add_arguments(self, parser):
        pass
        # parser.add_argument('sample', nargs='+')

    # def handle(self, *args, **options):
    #     raise NotImplementedError()
    
    def handle(self, *args, **options):
        print("Deleting books...")
        Book.objects.all().delete()
        with open(get_path('data.csv'), 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            i = 0
            for row in reader:
                i += 1
                book = Book(
                    name=row['name'],
                    author=row['author'],
                    description=row['description'],
                    category=row['category'],
                    url=row['url'],
                    date=row['date'],
                )
                book.save()
        print(f"{i} books loaded!")