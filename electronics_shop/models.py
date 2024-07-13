from django.db import models

NULLABLE = {'null': True, 'blank': True}
TYPE_CHOICES = (
    ('1', 'factory'),
    ('2', 'mass retailer'),
    ('3', 'self-employed'),
)
LEVEL_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
)


# Create your models here.
class Supplier(models.Model):
    type = models.CharField(choices=TYPE_CHOICES)
    level = models.SmallIntegerField(choices=LEVEL_CHOICES)
    title = models.CharField(max_length=150, verbose_name='Title')
    email = models.EmailField(verbose_name='E-mail')
    country = models.CharField(max_length=150, verbose_name='Country')
    city = models.CharField(max_length=150, verbose_name='City')
    street = models.CharField(max_length=150, verbose_name='Street')
    house_number = models.CharField(max_length=150, verbose_name='Number of a house')
    product = models.ManyToManyField(
        'Product', **NULLABLE, on_delete=models.SET_NULL, verbose_name='Product')
    supplier = models.ForeignKey(
        'Supplier', **NULLABLE, on_delete=models.SET_NULL, verbose_name='Supplier')
    debt = models.DecimalField(max_digits=11, decimal_places=2, default=0.00, verbose_name='Debt')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation time')

    def __str__(self):
        return f'{self.level} {self.type} {self.title}'

    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'
        ordering = ('title',)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    model = models.CharField(max_length=150, verbose_name='Model')
    date = models.DateField(default='', **NULLABLE, verbose_name='Release date')

    def __str__(self):
        return f'{self.title} {self.model}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('title', 'model',)
