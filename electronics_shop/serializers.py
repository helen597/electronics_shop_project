from rest_framework import serializers

from electronics_shop.models import Product, Supplier
from electronics_shop.validators import SupplierValidator


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "title", "model", "date",)


class SupplierSerializer(serializers.ModelSerializer):
    products = ProductSerializer(
        source='product_set.all', many=True, read_only=True
    )

    class Meta:
        model = Supplier
        fields = (
            "id",
            "type",
            "level",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "debt",
            "created_at",
            "the_supplier",
            "products",
        )
        validators = [SupplierValidator(field="the_supplier")]


class SupplierUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "type",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "the_supplier",
        ]
        validators = [SupplierValidator(field="the_supplier")]
