from django.contrib.contenttypes.models import ContentType
from django.core import management
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Restores DB from json file. Files must be called "backup.json" on manage.py level'

    def handle(self, *args, **options):
        management.call_command("makemigrations")
        management.call_command("migrate")
        ContentType.objects.all().delete()
        management.call_command("loaddata", "backup.json")
        print("Restore")