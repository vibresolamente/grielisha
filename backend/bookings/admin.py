from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'status', 'booking_date', 'booking_time', 'total_price', 'created_at')
    list_filter = ('status', 'service', 'created_at')
    search_fields = ('user__email', 'user__username', 'service__name', 'location')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    actions = ['confirm_bookings', 'mark_as_completed', 'cancel_bookings']

    fieldsets = (
        ('Booking Status', {
            'fields': ('status',)
        }),
        ('User & Service', {
            'fields': ('user', 'service', 'total_price')
        }),
        ('Schedule & Location', {
            'fields': ('booking_date', 'booking_time', 'location', 'notes')
        }),
        ('System Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def confirm_bookings(self, request, queryset):
        queryset.update(status='paid')
    confirm_bookings.short_description = "Confirm bookings (Marks as Paid)"

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = "Mark selected bookings as Completed"

    def cancel_bookings(self, request, queryset):
        queryset.update(status='cancelled')
    cancel_bookings.short_description = "Cancel selected bookings"
