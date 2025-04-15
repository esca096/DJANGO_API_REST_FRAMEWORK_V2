from api.models import Product
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api.serializers import ProductSerializer1, ProductSerializer2

#comment developper une api rest avec le decorateur api_view

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def product_api_view(request, pk=None, *args, **kwargs):
    
    if request.method == 'GET':
        # If a pk is provided, return the specific product
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer1(product, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        # If no pk is provided, return all products
        products = Product.objects.all()
        context = {'request': request}
        serializer = ProductSerializer1(products, many=True, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        name = data.get('name')
        serializer = ProductSerializer1(data=request.data,  context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        if pk is None:
            return Response({"error": "ID is required for this request"}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer1(product, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        if pk is None:
            return Response({"error": "ID is required for this request"}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        if pk is None:
            return Response({"error": "ID is required for this request"}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer1(product, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)