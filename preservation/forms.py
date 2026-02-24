from django import forms
from .models import PreservationRecord


class PreservationForm(forms.ModelForm):
    class Meta:
        model = PreservationRecord
        fields = ['check_date', 'condition', 'current_location', 'is_on_display', 'restoration_notes']

        widgets = {
            'check_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
            'current_location': forms.TextInput(attrs={'class': 'form-input'}),
            'restoration_notes': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'is_on_display': forms.CheckboxInput(attrs={'class': 'form-checkbox'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['check_date'].disabled = True
            self.fields['check_date'].help_text = "The inspection date cannot be changed after creation."