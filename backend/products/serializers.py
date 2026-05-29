from rest_framework import serializers
from .models import Product, Category, Wishlist

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category_name', 'image', 'stock_quantity', 'is_active', 'is_featured', 'tags', 'rating', 'reviews_count')

class WishlistSerializer(serializers.ModelSerializer):
    product_details = ProductListSerializer(source='products', many=True, read_only=True)
    
    class Meta:
        model = Wishlist
        fields = ('id', 'user', 'products', 'services', 'product_details', 'updated_at')
        read_only_fields = ('user',)

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    is_in_stock = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
