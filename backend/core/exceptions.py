from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging
import uuid

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    # Call standard DRF exception handler first
    response = exception_handler(exc, context)
    
    # Generate a unique trace ID for this error
    trace_id = str(uuid.uuid4())
    
    if response is None:
        # This is a server-side error (500) that DRF didn't catch
        logger.error(f"Unhandled Exception: {exc} | Trace: {trace_id}", exc_info=True)
        return Response({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred in the ecosystem.',
            'trace_id': trace_id,
            'status_code': 500
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Standardize the error response for handled exceptions
    response.data = {
        'error': response.status_text,
        'message': response.data if isinstance(response.data, (dict, list)) else str(response.data),
        'trace_id': trace_id,
        'status_code': response.status_code
    }
    
    return response
