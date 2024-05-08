from django.db import models
from decimal import Decimal


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
    ape_image = models.ImageField()
    one_ape_milk_consumption_per_second = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal('0.014'))
    ape_speed = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    ape_carry_capacity = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    ape_attack_value = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    ape_defense_value = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    ape_life = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('100'))
    clay_mining_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    metal_mining_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    stone_mining_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    hay_gathering_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    milking_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    wood_cutting_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('1'))
    special_hay_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0'))
    construction_wood_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0'))
    tool_wood_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0'))
    bricks_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0'))
    construction_stone_producing_efficiency_units_per_second = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0'))
    unit_production_time = models.TimeField()
    buy_cost_in_milk = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('20'))
    buy_cost_in_hay = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('15'))
    buy_cost_in_wood = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('25'))
    buy_cost_in_clay = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('10'))
    buy_cost_in_stone = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('5'))
    buy_cost_in_metal = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('3'))
