from rest_framework.response import Response
from rest_framework import serializers, status
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

    def perform_create(self, serializer):
        try:
            supplier = serializer.save()
            if not supplier.the_supplier:
                supplier.level = 0
            elif supplier.the_supplier.level == 0:
                supplier.level = 1
            elif supplier.the_supplier.level == 1:
                supplier.level = 2
        except serializers.ValidationError('Выберите другого поставщика') as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SupplierUpdateAPIView(UpdateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()

    def perform_update(self, serializer):
        pass


class SupplierDestroyAPIView(DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objecs.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
