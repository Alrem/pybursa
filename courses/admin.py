from django.contrib import admin

# Register your models here.
from courses.models import Courses

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    radio_fields = {"instructor": admin.HORIZONTAL,
                    "assistant": admin.HORIZONTAL,
                    "venue": admin.VERTICAL,}
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'description', 'instructor', 'assistant', 'start_date', 'end_date', 'technology', 'venue']
    list_display_links = ['title', 'description']
    ordering = ['start_date', 'title', 'instructor']
    list_filter = ['title', 'description', 'instructor', 'assistant', 'start_date', 'end_date', 'technology', 'venue']
    search_fields = ['title', 'description']
