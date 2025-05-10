from django.core.management.base import BaseCommand
from monitor.models import Credential
from monitor.utils import check_hibp  # Ensure this exists

class Command(BaseCommand):
    help = 'Check all credentials for breaches'

    def handle(self, *args, **options):
        for credential in Credential.objects.all():
            is_breached, breaches = check_hibp(credential.email)
            if is_breached:
                credential.is_breached = True
                credential.save()
                self.stdout.write(f"Breach detected for {credential.email}")
