from api.models import Product
from rest_framework import serializers

# create user information for viewst model
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    #author_products = serializers.PrimaryKeyRelatedField(many=True, read_only=True,source='product_set') permet de recuperer les produits lier a lutilisateur facon simple
    author_products = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'author_products']
    
    # recuperer les produits lier a lutilisateur 
    def get_author_products(self, obj):
        products = obj.product_set.all()
        context = self.context
        return ProductSerializer2(products, many=True, context=context).data
        

# ce Serializer est res important le bon foctionnnement de l'api
class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(max_length=255)
    price_in_euros = serializers.SerializerMethodField()
    description_in_euros = serializers.SerializerMethodField()
    #detail_link = serializers.CharField(source='get_absolute_url', read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    author = UserSerializer()
    
    class Meta:
        model = Product
        fields = ['id', 'name','price', 'description','email', 'price_in_euros', 'description_in_euros', 'link', 'author']
        #read_only_fields = ['created_at', 'updated_at']
    
    def get_price_in_euros(self, obj):
        return obj.get_price_in_euros()
        
    def get_description_in_euros(self, obj):
        return obj.get_description()
    
    # def get_detail_link(self, obj):
    #     return obj.get_absolute_url()
        
    def validate_name(self, value):
        if value in ["escanor", "lion", 'toshi']:
            raise serializers.ValidationError("Name is not allowed")
        return value
        
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        print("Email", email)
        
        #connected user
        user = self.context['request'].user
        print("User", user)
        validated_data['author'] = user
        return super().create(validated_data)


# lier User qui permet de recuperer les produits lier a lutilisateur
class ProductSerializer2(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    class Meta:
        model = Product
        fields = ['id', 'name', 'price','link']



# class ProductSerializer2(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     description = serializers.CharField()
        