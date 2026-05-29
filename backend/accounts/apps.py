from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals
        from .provisioner import ensure_admin_accounts
        try:
            ensure_admin_accounts()
        except Exception as e:
            # Log the exact failure reason to the server console
            print(f"GRIELISHA STARTUP ERROR: {str(e)}")
