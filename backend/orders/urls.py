from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('cart/<int:pk>/', views.UpdateCartItemView.as_view(), name='cart-item-detail'),
    path('create/', views.create_order, name='create-order'),
    path('', views.OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/reorder/', views.ReorderView.as_view(), name='order-reorder'),
    path('payments/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('payments/admin/', views.PaymentAdminListView.as_view(), name='payment-admin-list'),
    path('payments/<int:pk>/verify/', views.verify_payment, name='payment-verify'),
]
