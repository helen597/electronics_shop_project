from rest_framework import serializers


class SupplierValidator:
    """Нельзя выбирать поставщика с уровнем 2
    ввиду ограничения количества уровней иерархии"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        the_supplier = value.get(self.field)
        if the_supplier and the_supplier.level == 2:
            raise serializers.ValidationError('Выберите другого поставщика')
