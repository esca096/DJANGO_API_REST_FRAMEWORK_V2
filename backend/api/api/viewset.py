from api.models import Product
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from api.api.serializers import ProductSerializer1
from rest_framework.decorators import action


class ProductViewSet(ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    serializer_class = ProductSerializer1
    queryset = Product.objects.all()
    
    
    #router pour les products produit superieur a 100
    @action(detail=False, methods=['GET'], url_path='expensive-products', url_name='expensive-products')
    def expensive_products(self, request, *args, **kwargs):
        products = Product.objects.filter(price__gte=100)
        serializer = ProductSerializer1(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #permet d'afficher les produits superieur ou inferieur avec la "get out lte" a 100
    # def get_queryset(self):
    #     return super().get_queryset().filter(price__lte=100)