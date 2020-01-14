from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    prices = serializers.SlugRelatedField(many=True, read_only=True, slug_field='price')

    class Meta:
        model = Product
        fields = "__all__"


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = '__all__'
