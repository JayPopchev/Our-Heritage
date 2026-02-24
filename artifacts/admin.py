from django.contrib import admin

# Register your models here.
from django.contrib import admin

from preservation.models import PreservationRecord
from .models import Artifact, Exhibition
from resources.models import ArtifactResource

class ArtifactResourceInline(admin.TabularInline):
    model = ArtifactResource
    extra = 3
    fields = ['description', 'image_url']

class PreservationRecordInline(admin.TabularInline):
    model = PreservationRecord
    extra = 1
    fields = ['check_date', 'condition', 'current_location', 'is_on_display']


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'material']
    inlines = [ArtifactResourceInline, PreservationRecordInline]

admin.site.register(Exhibition)