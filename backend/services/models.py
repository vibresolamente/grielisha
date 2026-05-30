from django.db import models
from django.core.validators import MinValueValidator

class Service(models.Model):
    SERVICE_CHOICES = [
        ('car_detailing', 'Car Detailing'),
        ('office_cleaning', 'Office Deep Cleaning'),
        ('house_cleaning', 'House Cleaning'),
        ('compound_cleaning', 'Compound Cleaning'),
        ('graphic_design', 'Graphic Design'),
        ('website_development', 'Website Development'),
        ('system_development', 'System Development'),
        ('chauffeur_services', 'Chauffeur Services'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, unique=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    duration_hours = models.PositiveIntegerField(help_text="Estimated duration in hours")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma separated tags")
    features = models.JSONField(default=list, blank=True)
    specifications = models.JSONField(default=dict, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)
    reviews_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
