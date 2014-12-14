from django.contrib import admin

# Register your models here.
from address.models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['postal_code', 'country', 'region', 'district', 'street', 'home']
    list_display_links = ['postal_code', 'country', 'region', 'district', 'street', 'home']
    ordering = ['country', 'street']
    list_filter = ['postal_code', 'country', 'region', 'district', 'street', 'home']
    search_fields = ['country', 'street']