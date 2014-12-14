from django.contrib import admin

# Register your models here.
from students.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    radio_fields = {"dossier": admin.HORIZONTAL}
    filter_horizontal = ['courses']
    list_display = ['name', 'surname', 'email', 'phone', 'package', 'dossier']
    list_display_links = ['name', 'surname',]
    ordering = ['surname', 'name']
    list_filter = ['name', 'surname', 'email', 'phone', 'package', 'dossier']
    search_fields = ['name', 'surname']
    