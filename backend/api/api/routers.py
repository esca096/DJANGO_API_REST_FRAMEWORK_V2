from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from api.api.viewset import ProductViewSet 

"""
default router pour les operations CRUD
simple router pour les operations de lecture
"""

router = DefaultRouter()
router.register('v1/product', ProductViewSet, basename='product')

urlpatterns = router.urls