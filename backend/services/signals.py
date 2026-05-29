from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Service
from accounts.models import ActivityLog

@receiver(post_save, sender=Service)
def log_service_changes(sender, instance, created, **kwargs):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    admin = User.objects.filter(is_staff=True).first()
    
    if admin:
        verb = "created" if created else "updated"
        ActivityLog.objects.create(
            user=admin,
            action='admin_action',
            description=f"Service '{instance.name}' was {verb}. Price: KES {instance.base_price}"
        )
