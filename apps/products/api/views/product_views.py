from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import permission_classes

from apps.base.api import (
    # GeneralList,
    # GeneralDetail,
    # GeneralViewSet
    GeneralViewSet)
from apps.products.api.serializers.product_serializers import ProductSerializer
# from apps.products.models import Product

from apps.users.authentication_mixins import Authentication


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = 'Solo el autor puede modificar el elemento'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


# class ProductViewSet(Authentication, GeneralViewSet):
class ProductViewSet(GeneralViewSet, IsOwnerOrReadOnly):
# class ProductViewSet(GeneralViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # queryset = ProductSerializer.Meta.model.objects.filter(state=True)

# class ProductViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = ProductSerializer.Meta.model.objects.filter(state=True)


# class ProductList(GeneralList):
#     # queryset = Product.objects.filter(state=True)
#     serializer_class = ProductSerializer
#
#
# class ProductDetail(GeneralDetail):
#     # queryset = Product.objects.all()
#     serializer_class = ProductSerializer
