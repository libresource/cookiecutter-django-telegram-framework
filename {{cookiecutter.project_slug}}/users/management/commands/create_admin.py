from django.core.management.base import BaseCommand
from django.conf import settings
from users.scripts import create_admin


class Command(BaseCommand):
    help = 'Create main admin'

    def handle(self, *args, **options):
        try:
            username = settings.ADMIN_USERNAME
            password = settings.ADMIN_PASSWORD
            email = settings.ADMIN_EMAIL
        except AttributeError:
            self.stdout.write(
                self.style.ERROR('ADMIN DATA WAS NOT SET')
            )
        else:
            admin, created = create_admin(username, password, email)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'ADMIN {admin.username} was created')
                )
            self.stdout.write(
                self.style.SUCCESS(f'ADMIN {admin.username} already exists')
            )
