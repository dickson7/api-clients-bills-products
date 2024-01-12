from rest_framework import serializers
from .models import Client, Product, Bill, BillProduct
import csv

class CSVClientSerializer(serializers.Serializer):
    document = serializers.CharField()
    full_name = serializers.CharField()
    num_bills = serializers.IntegerField()

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BillProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = BillProduct
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    products = BillProductSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = '__all__'