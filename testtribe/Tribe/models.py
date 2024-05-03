from django.db import models


# Create your models here.
class Notes(models.Model):
    """
    Creates user notes for the user
    """
    text = models.CharField(max_length=300)

class Resources(models.Model):
    resource_name = models.CharField(max_length=100)
    resource_image = models.ImageField()
    max_storage_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    stored_resource_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    stored_resource_quantity_at_time = models.DateTimeField()
    production_per_second = models.DecimalField(max_digits=10, decimal_places=2)
    consumption_per_second = models.DecimalField(max_digits=10, decimal_places=2)
    net_production_per_second = models.DecimalField(max_digits=10, decimal_places=2)
    one_unit_weight = models.DecimalField(max_digits=10, decimal_places=2)
