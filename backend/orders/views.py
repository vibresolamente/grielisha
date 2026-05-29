from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db import transaction
from .models import Order, OrderItem, Cart, CartItem, Payment
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer, CreateOrderSerializer, PaymentSerializer

class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        product = serializer.validated_data.get('product')
        service = serializer.validated_data.get('service')
        quantity = serializer.validated_data.get('quantity', 1)
        
        if not product and not service:
            raise serializer.ValidationError("Either product or service must be provided")

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            service=service,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

class UpdateCartItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@transaction.atomic
def create_order(request):
    serializer = CreateOrderSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        cart, created = Cart.objects.get_or_create(user=request.user)
        total_amount = cart.total_amount
        
        order = Order.objects.create(
            user=request.user,
            total_amount=total_amount,
            shipping_address=serializer.validated_data['shipping_address'],
            full_name=serializer.validated_data['full_name'],
            phone=serializer.validated_data['phone'],
            email=serializer.validated_data['email'],
            city=serializer.validated_data['city'],
            postal_code=serializer.validated_data['postal_code']
        )
        
        for cart_item in cart.items.all():
            price = cart_item.product.price if cart_item.product else cart_item.service.base_price
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                service=cart_item.service,
                quantity=cart_item.quantity,
                price=price
            )
        
        cart.items.all().delete()
        
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all().order_by('-created_at')
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class OrderDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        order = serializer.validated_data['order']
        # Set order status to pending_payment
        order.status = 'pending_payment'
        order.save()
        serializer.save(user=self.request.user)

class PaymentAdminListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Payment.objects.all().order_by('-created_at')
    filterset_fields = ['status', 'payment_method']

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
@transaction.atomic
def verify_payment(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
        action = request.data.get('action') # 'verify' or 'reject'
        
        if action == 'verify':
            payment.status = 'verified'
            if payment.order:
                payment.order.status = 'paid'
                payment.order.save()
            if payment.booking:
                payment.booking.status = 'paid'
                payment.booking.save()
        elif action == 'reject':
            payment.status = 'rejected'
            if payment.order:
                payment.order.status = 'rejected'
                payment.order.save()
            if payment.booking:
                payment.booking.status = 'rejected'
                payment.booking.save()
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
            
        payment.save()
        return Response(PaymentSerializer(payment).data)
    except Payment.DoesNotExist:
        return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

class ReorderView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    @transaction.atomic
    def post(self, request, pk):
        try:
            old_order = Order.objects.get(pk=pk, user=request.user)
            cart, created = Cart.objects.get_or_create(user=request.user)
            
            for item in old_order.items.all():
                cart_item, created = CartItem.objects.get_or_create(
                    cart=cart,
                    product=item.product,
                    service=item.service,
                    defaults={'quantity': item.quantity}
                )
                if not created:
                    cart_item.quantity += item.quantity
                    cart_item.save()
            
            return Response({'message': 'Success! Items added to cart.'})
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
