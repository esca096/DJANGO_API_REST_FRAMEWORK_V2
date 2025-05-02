from django.urls import path, include
from .views import home
from api.api.api import product_api_view

from api.api.mixins import (ProductListApiView, 
                            ProductDetailApiView, 
                            ProductCreateApiView, 
                            ProductUpdateApiView, 
                            ProductDeleteApiView,
                            CombineApiVIewSet,
                            )

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'
urlpatterns = [
    #permet de recuperer le token d'authentificationpour thunder client
    path('api-auth-token/', obtain_auth_token, name='api_obtain_auth_token'),
    
    #url with api_view
    path('', home, name='home'),
    path('product/', product_api_view, name='product_api'),
    path('product/<int:pk>/', product_api_view, name='product_api_view_detail'),
    
    # url with routers v1 modelviewset
    path('', include('api.api.routers')),
    
    # url with mixins
    path('v2/product-list/', ProductListApiView.as_view(), name='product_list_api_view'),
    path('v2/product-detail/<int:pk>/', ProductDetailApiView.as_view(), name='product_detail_api_view'),
    path('v2/product-create/', ProductCreateApiView.as_view(), name='product_create_api_view'),
    path('v2/product-update/<int:pk>/', ProductUpdateApiView.as_view(), name='product_update_api_view'),
    path('v2/product-delete/<int:pk>/', ProductDeleteApiView.as_view(), name='product_delete_api_view'),
    
    # url with mixins comine
    path('v3/product-combine/', CombineApiVIewSet.as_view(), name='product_combine_api_view'),
    path('v3/product-combine/<int:pk>/', CombineApiVIewSet.as_view(), name='product_combine_api_view_detail'),
    
]
