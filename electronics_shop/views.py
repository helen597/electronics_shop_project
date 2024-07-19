from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from electronics_shop.models import Supplier, Product
from electronics_shop.serializers import (
    SupplierSerializer,
    ProductSerializer,
    SupplierUpdateSerializer,
)
from rest_framework.filters import SearchFilter
from electronics_shop.permissions import IsActiveUser


# Create your views here.
class SupplierListAPIView(ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()
    permission_classes = [IsActiveUser]
    filter_backends = [SearchFilter]
    search_fields = ["country"]


class SupplierRetrieveAPIView(RetrieveAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()
    permission_classes = [IsActiveUser]


class SupplierCreateAPIView(CreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()
    permission_classes = [IsActiveUser]

    def perform_create(self, serializer):
        supplier = serializer.save()
        if not supplier.the_supplier:
            supplier.level = 0
        elif supplier.the_supplier.level == 0:
            supplier.level = 1
        elif supplier.the_supplier.level == 1:
            supplier.level = 2
        supplier.save()


class SupplierUpdateAPIView(UpdateAPIView):
    serializer_class = SupplierUpdateSerializer
    queryset = Supplier.objecs.all()
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
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()
    permission_classes = [IsActiveUser]


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]
