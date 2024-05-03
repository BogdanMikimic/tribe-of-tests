from django.contrib import admin
from Tribe.models import Notes, Resources
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