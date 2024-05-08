from django.contrib import admin
from Tribe.models import *
# Register your models here.


class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('resource_name',
                    'max_storage_capacity',
                    'stored_resource_quantity',
                    'production_per_second',
                    'consumption_per_second',
                    'net_production_per_second',
                    'one_unit_weight')
    list_filter = ('one_unit_weight', 'net_production_per_second')  # Filters on the right-hand sidebar
    search_fields = ('resource_name',)  # Searchable fields

admin.site.register(Resources, ResourcesAdmin)

class ApesAdmin(admin.ModelAdmin):
    list_display = ('ape_type_name',
                    'how_many_apes_of_that_type',
                    'one_ape_milk_consumption_per_second',
                    'ape_speed',
                    'ape_carry_capacity',
                    'ape_attack_value',
                    'ape_defense_value',
                    'ape_life')
    search_fields = ('ape_type_name',)

admin.site.register(Apes, ApesAdmin)