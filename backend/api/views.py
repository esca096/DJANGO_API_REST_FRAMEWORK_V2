from django.shortcuts import render

# Retourne des donner sous le format Json
from django.http import JsonResponse

#import du crsf pour la securite
from django.views.decorators.csrf import csrf_exempt

# import extion JSON
import json

#Importation du models
from .models import Product


# Create your views here.
@csrf_exempt
def home(request):
    headers =  request.headers
    params = request.GET
    if request.method == 'POST':
        post_data = request.body
        data = json.loads(post_data)
        
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        
        product = Product.objects.create(
            name=name,
            price=price,
            description=description
        )
        
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        })
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
    return JsonResponse(data, safe=False)