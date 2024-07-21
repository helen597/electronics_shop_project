from rest_framework.filters import SearchFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from electronics_shop.models import Product, Supplier
from electronics_shop.permissions import IsActiveUser
from electronics_shop.serializers import (ProductSerializer,
                                          SupplierSerializer,
                                          SupplierUpdateSerializer)


# Create your views here.
class SupplierListAPIView(ListAPIView):
    """Supplier list controller"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [SearchFilter]
    search_fields = ["country"]


class SupplierRetrieveAPIView(RetrieveAPIView):
    """Supplier retrieve controller"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser]


class SupplierCreateAPIView(CreateAPIView):
    """Supplier create controller"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser]

    def perform_create(self, serializer):
        supplier = serializer.save()
        if not supplier.the_supplier:
            supplier.level = 0
            supplier.debt = 0
        elif supplier.the_supplier.level == 0:
            supplier.level = 1
        elif supplier.the_supplier.level == 1:
            supplier.level = 2
        supplier.save()


class SupplierUpdateAPIView(UpdateAPIView):
    """Supplier update controller"""
    serializer_class = SupplierUpdateSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser]

    def perform_update(self, serializer):
        supplier = serializer.save()
        if not supplier.the_supplier:
            supplier.level = 0
        elif supplier.the_supplier.level == 0:
            supplier.level = 1
        elif supplier.the_supplier.level == 1:
            supplier.level = 2
        supplier.save()


class SupplierDestroyAPIView(DestroyAPIView):
    """Supplier delete controller"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser]


class ProductListAPIView(ListAPIView):
    """Product list controller"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]
