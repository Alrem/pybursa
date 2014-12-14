from django.contrib import admin

# Register your models here.
from coaches.models import Coaches

@admin.register(Coaches)
class CoachesAdmin(admin.ModelAdmin):
    radio_fields = {"user": admin.HORIZONTAL,
                    "role": admin.HORIZONTAL,
                    "dossier": admin.HORIZONTAL,}
    list_display = ['name', 'surname', 'email', 'phone', 'role', 'user', 'dossier']
    list_display_links = ['name', 'surname', 'email', 'phone', 'role', 'user', 'dossier']
    ordering = ['name', 'surname', 'email', 'phone', 'role', 'user', 'dossier']
    list_filter = ['role', 'name', 'surname']
    search_fields = ['name', 'surname']