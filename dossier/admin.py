from django.contrib import admin

# Register your models here.
from dossier.models import Dossier

@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    radio_fields = {"address": admin.HORIZONTAL,
                    "color": admin.HORIZONTAL,
                    }
    filter_horizontal = ['unloved_courses']
    list_display = ['address', 'color']
    list_display_links = ['address', 'color']
    ordering = ['address', 'color']
    list_filter = ['address', 'color']
    search_fields = ['address', 'color']

