from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceListCreateView.as_view(), name='service-list'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('bulk-action/', views.ServiceBulkActionView.as_view(), name='service-bulk-action'),
]
