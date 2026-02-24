from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PreservationRecord


@admin.register(PreservationRecord)
class PreservationRecordAdmin(admin.ModelAdmin):
    # Displays these columns in the admin list view
    list_display = ['artifact', 'check_date', 'condition', 'is_on_display']

    # Adds a sidebar filter for dates and conditions
    list_filter = ['check_date', 'condition', 'is_on_display']

    # Allows searching by artifact title
    search_fields = ['artifact__title']