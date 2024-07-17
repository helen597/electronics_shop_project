from rest_framework import serializers
from electronics_shop.models import Supplier, Product
from validators import SupplierValidator


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'
        validators = [SupplierValidator(field='the_supplier')]


class SupplierUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = [
            'type', 'title', 'email', 'country',
            'city', 'street', 'house_number', 'the_supplier'
        ]
        validators = [SupplierValidator(field='the_supplier')]


class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
