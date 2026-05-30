from rest_framework import serializers
from .models import Order, OrderItem, Cart, CartItem, Payment
from products.models import Product

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'order', 'booking', 'payment_method', 'transaction_code', 'amount', 'status', 'created_at', 'updated_at')
        read_only_fields = ('user', 'status', 'created_at', 'updated_at')

class CartItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    subtotal = serializers.ReadOnlyField()
    item_type = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'service', 'name', 'price', 'quantity', 'subtotal', 'item_type', 'added_at')
        read_only_fields = ('added_at',)

    def get_name(self, obj):
        if obj.product:
            return obj.product.name
        elif obj.service:
            return obj.service.name
        return "Unknown"

    def get_price(self, obj):
        if obj.product:
            return obj.product.price
        elif obj.service:
            return obj.service.base_price
        return 0

    def get_item_type(self, obj):
        return "product" if obj.product else "service"

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_amount = serializers.ReadOnlyField()
    item_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Cart
        fields = ('id', 'items', 'total_amount', 'item_count', 'created_at', 'updated_at')

class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    subtotal = serializers.ReadOnlyField()
    
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'service', 'name', 'quantity', 'price', 'subtotal')

    def get_name(self, obj):
        if obj.product:
            return obj.product.name
        elif obj.service:
            return obj.service.name
        return "Unknown"

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    payment = PaymentSerializer(read_only=True)
    item_count = serializers.ReadOnlyField()
    user_email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = Order
        fields = (
            'id', 'user', 'user_email', 'status', 'total_amount', 'shipping_address', 
            'full_name', 'phone', 'email', 'city', 'postal_code', 
            'delivery_status', 'transport_provider', 'tracking_number', 'delivery_origin', 'estimated_delivery_date',
            'items', 'item_count', 'payment', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'user', 'total_amount', 'created_at', 'updated_at'
        )

class CreateOrderSerializer(serializers.Serializer):
    shipping_address = serializers.CharField(max_length=500)
    full_name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    city = serializers.CharField(max_length=100)
    postal_code = serializers.CharField(max_length=20)
    
    def validate(self, attrs):
        user = self.context['request'].user
        try:
            cart = user.cart
            if not cart.items.exists():
                raise serializers.ValidationError("Cart is empty")
        except Cart.DoesNotExist:
            raise serializers.ValidationError("Cart not found")
        return attrs
