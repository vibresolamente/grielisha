from rest_framework import serializers
from .models import Booking
from services.models import Service
from orders.serializers import PaymentSerializer

class BookingSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    payment = PaymentSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = ('id', 'user', 'user_email', 'service', 'service_name', 'status', 'booking_date', 'booking_time', 'location', 'notes', 'total_price', 'payment', 'created_at', 'updated_at')
        read_only_fields = ('user', 'total_price', 'created_at', 'updated_at')

class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('service', 'booking_date', 'booking_time', 'location', 'notes')
    
    def validate(self, attrs):
        service = attrs['service']
        if not service.is_active:
            raise serializers.ValidationError("This service is not available")
        return attrs
