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

class Apes(models.Model):
    ape_type_name = models.CharField(max_length=30)
    how_many_apes_of_that_type = models.IntegerField()
    ape_speed = models.DecimalField(max_digits=5, decimal_places=2)
    ape_carry_capacity = models.DecimalField(max_digits=5, decimal_places=2)
    ape_attack_value = models.DecimalField(max_digits=5, decimal_places=2)
    ape_defense_value = models.DecimalField(max_digits=5, decimal_places=2)
    ape_life = models.DecimalField(max_digits=5, decimal_places=2)
    clay_mining_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    metal_mining_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    stone_mining_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    hay_gathering_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    milking_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    wood_cutting_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    special_hay_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    construction_wood_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    tool_wood_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
    bricks_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2)
