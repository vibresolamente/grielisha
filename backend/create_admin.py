import os
import django
import sys

# Set up django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grielisha.settings')
django.setup()

from accounts.models import User

def create_accounts():
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
        status = "Created" if created else "Updated"
        print(f"Account {acc['email']}: {status}")

if __name__ == "__main__":
    create_accounts()
