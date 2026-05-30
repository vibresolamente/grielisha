from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Service
from .serializers import ServiceSerializer, ServiceListSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ServiceListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['service_type']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'base_price', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        if self.request.user and self.request.user.is_authenticated and self.request.user.is_staff:
            return Service.objects.all()
        return Service.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceListSerializer
        return ServiceSerializer

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ServiceBulkActionView(APIView):
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request):
        ids = request.data.get('ids', [])
        action = request.data.get('action')
        
        if not ids or not action:
            return Response({'error': 'Missing ids or action'}, status=status.HTTP_400_BAD_REQUEST)
            
        services = Service.objects.filter(id__in=ids)
        
        if action == 'delete':
            services.delete()
            return Response({'message': f'Successfully deleted {len(ids)} services'})
        elif action == 'set_active':
            services.update(is_active=True)
            return Response({'message': f'Set {len(ids)} services to active'})
        elif action == 'set_inactive':
            services.update(is_active=False)
            return Response({'message': f'Set {len(ids)} services to inactive'})
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
