from django.contrib import admin
from .models import Order, OrderItem, Cart, CartItem, Payment

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('subtotal',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'delivery_status', 'total_amount', 'created_at')
    list_filter = ('status', 'delivery_status', 'created_at')
    search_fields = ('user__email', 'user__username', 'tracking_number', 'transport_provider')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [OrderItemInline]
    actions = ['mark_as_shipped', 'mark_as_delivered']
    
    fieldsets = (
        ('Order Info', {
            'fields': ('user', 'status', 'total_amount', 'created_at', 'updated_at')
        }),
        ('Customer details', {
            'fields': ('full_name', 'email', 'phone', 'shipping_address', 'city', 'postal_code')
        }),
        ('Logistics & Delivery', {
            'fields': ('delivery_status', 'transport_provider', 'tracking_number', 'delivery_origin', 'estimated_delivery_date')
        }),
    )

    def mark_as_shipped(self, request, queryset):
        queryset.update(delivery_status='dispatched')
    mark_as_shipped.short_description = "Mark selected orders as Dispatched"

    def mark_as_delivered(self, request, queryset):
        queryset.update(delivery_status='delivered', status='delivered')
    mark_as_delivered.short_description = "Mark selected orders as Delivered"

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'user', 'payment_method', 'transaction_code', 'amount', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('user__email', 'transaction_code', 'order__id')
    readonly_fields = ('created_at', 'updated_at')
    actions = ['approve_payments', 'reject_payments']

    def approve_payments(self, request, queryset):
        for payment in queryset:
            payment.status = 'verified'
            payment.save()
            # Synchronize order or booking status
            if payment.order:
                payment.order.status = 'paid'
                payment.order.save()
            if payment.booking:
                payment.booking.status = 'paid'
                payment.booking.save()
    approve_payments.short_description = "Approve payments (Syncs Order/Booking)"

    def reject_payments(self, request, queryset):
        for payment in queryset:
            payment.status = 'rejected'
            payment.save()
            # Synchronize order or booking status
            if payment.order:
                payment.order.status = 'rejected'
                payment.order.save()
            if payment.booking:
                payment.booking.status = 'rejected'
                payment.booking.save()
    reject_payments.short_description = "Reject payments (Syncs Order/Booking)"

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('cart__user__email', 'product__name')
    ordering = ('-added_at',)

