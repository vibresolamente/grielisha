import logging
from django.db.utils import IntegrityError
from django.apps import apps

logger = logging.getLogger(__name__)

def ensure_admin_accounts():
    """
    Forceful provisioner that ensures Admin and Staff accounts exist.
    Returns a status dictionary for reporting.
    """
    results = []
    try:
        # Late binding retrieval of User model
        User = apps.get_model('accounts', 'User')
    except (LookupError, RuntimeError) as e:
        return {'status': 'error', 'message': f'App Registry Not Ready: {str(e)}'}

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
            # Use update_or_create to FORCE the state
            user, created = User.objects.update_or_create(
                email=acc['email'],
                defaults={
                    'username': acc['username'],
                    'is_staff': acc['is_staff'],
                    'is_superuser': acc['is_superuser'],
                    'role': acc['role']
                }
            )
            
            # Reset password to ensure it matches exactly
            user.set_password(acc['password'])
            user.save()
            
            status = "CREATED" if created else "UPDATED/RESTORED"
            results.append({'email': acc['email'], 'status': status})
            logger.info(f"GRIELISHA Provisioning: {acc['email']} {status}")
            
        except Exception as e:
            results.append({'email': acc['email'], 'status': 'error', 'error': str(e)})
            logger.error(f"GRIELISHA Provisioning Error for {acc['email']}: {str(e)}")

    return {'status': 'success', 'results': results}
