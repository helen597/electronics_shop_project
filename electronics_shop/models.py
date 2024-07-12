from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Supplier(models.Model):
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


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    model = models.CharField(max_length=150, verbose_name='Model')
    date = models.DateField(default='', **NULLABLE, verbose_name='Release date')
