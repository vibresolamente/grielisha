from django.http import JsonResponse
from accounts.provisioner import ensure_admin_accounts

def force_provision(request):
    """
    Emergency endpoint to manually trigger administrative provisioning.
    """
    result = ensure_admin_accounts()
    return JsonResponse(result)
