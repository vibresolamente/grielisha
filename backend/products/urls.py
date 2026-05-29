from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product-list'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('bulk-action/', views.ProductBulkActionView.as_view(), name='product-bulk-action'),
    path('recommendations/', views.RecommendationView.as_view(), name='product-recommendations'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('wishlist/toggle/', views.toggle_wishlist, name='wishlist-toggle'),
    path('stats/summary/', views.StatsSummaryView.as_view(), name='stats-summary'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
