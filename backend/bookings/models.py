from django.db import models
from django.contrib.auth import get_user_model
from services.models import Service

User = get_user_model()

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Confirmation'),
        ('pending_payment', 'Pending Payment Verification'),
        ('paid', 'Paid / Confirmed'),
        ('completed', 'Completed'),
        ('rejected', 'Payment Rejected'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    location = models.TextField()
    notes = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Booking {self.id} - {self.service.name} by {self.user.email}"
    
    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.service.base_price
        super().save(*args, **kwargs)
