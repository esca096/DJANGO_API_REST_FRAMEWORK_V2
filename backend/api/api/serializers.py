from api.models import Product
from rest_framework import serializers


class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        print("Email", email)
        return super().create(validated_data)
        

class ProductSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
        