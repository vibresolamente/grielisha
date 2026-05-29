from django.core.management.base import BaseCommand
from accounts.models import User
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Provisions default administrative and staff accounts for GRIELISHA.'

    def handle(self, *args, **kwargs):
        accounts = [
            {
                'email': 'admin@grielisha.com',
                'username': 'admin',
                'password': 'GrielishaAdmin2026!',
                'is_staff': True,
                'is_superuser': True,
                'role': 'admin'
            },
            {
                'email': 'staff@grielisha.com',
                'username': 'staff',
                'password': 'GrielishaStaff2026!',
                'is_staff': True,
                'is_superuser': False,
                'role': 'staff'
            }
        ]

        for acc in accounts:
            try:
                user, created = User.objects.get_or_create(
                    email=acc['email'],
                    defaults={
                        'username': acc['username'],
                        'is_staff': acc['is_staff'],
                        'is_superuser': acc['is_superuser'],
                        'role': acc['role']
                    }
                )
                user.set_password(acc['password'])
                user.save()
                
                status = "CREATED" if created else "UPDATED"
                self.stdout.write(self.style.SUCCESS(f'Account {acc["email"]} {status} successfully.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating {acc["email"]}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('GRIELISHA Administrative provisioning complete.'))
