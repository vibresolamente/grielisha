from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_admin_accounts(apps, schema_editor):
    User = apps.get_model('accounts', 'User')
    
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
        # In a historical model, we set the password field directly
        user.password = make_password(acc['password'])
        user.save()

def remove_admin_accounts(apps, schema_editor):
    User = apps.get_model('accounts', 'User')
    User.objects.filter(email__in=['admin@grielisha.com', 'staff@grielisha.com']).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_loyalty_points_alter_user_role_activitylog'),
    ]

    operations = [
        migrations.RunPython(create_admin_accounts, reverse_code=remove_admin_accounts),
    ]
