from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date']
        
    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Product name is required.")
        if not data.get('price'):
            raise serializers.ValidationError("Price is required.")
        if not data.get('stock_quantity'):
            raise serializers.ValidationError("Stock Quantity is required.")
        return data