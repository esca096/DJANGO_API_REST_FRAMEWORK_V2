from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from api.api.viewset import ProductViewSet, UserViewSet

"""
default router pour les operations CRUD
simple router pour les operations de lecture
c'est de facon que sont rengerister url des modelviewset
"""

router = DefaultRouter()
# permet de faire le CRUD sur les produits
router.register('v1/product', ProductViewSet, basename='product')
# permet d'afficher les produit lier a l'utilisateur
router.register('v1/user', UserViewSet, basename='user')

urlpatterns = router.urls