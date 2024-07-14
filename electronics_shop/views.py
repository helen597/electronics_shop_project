from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from electronics_shop.models import Supplier, Product
from electronics_shop.serializers import SupplierSerializer, ProductSerializer
from rest_framework.filters import SearchFilter


# Create your views here.
class SupplierListAPIView(ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()
    filter_backends = [SearchFilter]
    search_fields = ['country']


class SupplierRetrieveAPIView(RetrieveAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()


class SupplierCreateAPIView(CreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()


class SupplierUpdateAPIView(UpdateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()


class SupplierDestroyAPIView(DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
