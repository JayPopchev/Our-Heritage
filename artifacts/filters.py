# artifacts/filters.py
import django_filters
from django import forms
from .models import Artifact
from categories.models import Category

class ArtifactFilter(django_filters.FilterSet):
    # This creates the SEARCH BAR
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Search by name...', 'class': 'search-input'})
    )

    # This creates the MATERIAL filter (Dropdown or Checkboxes)
    # If you want CHECKBOXES, change forms.Select to forms.CheckboxSelectMultiple
    material = django_filters.ChoiceFilter(
        choices=Artifact.MaterialChoices,
        empty_label="All Materials"
    )

    # This creates the CATEGORY filter
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label="All Categories"
    )

    class Meta:
        model = Artifact
        fields = ['title', 'category', 'material']