from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, ActivityLog

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ActivityLog.objects.create(
        user=user,
        action='login',
        description=f"User {user.email} logged in successfully.",
        ip_address=request.META.get('REMOTE_ADDR')
    )

@receiver(post_save, sender=User)
def log_user_registration(sender, instance, created, **kwargs):
    if created:
        # Note: In a signal, there's no request object, so ip_address will be null
        # but we can track the event.
        ActivityLog.objects.create(
            user=instance,
            action='admin_action',
            description=f"New user account created for {instance.email}."
        )
