from django import forms
from .models import Artifact

class ArtifactForm(forms.ModelForm):
    # 1. Add our custom image_url field
    image_url = forms.URLField(
        required=False,
        label="Artifact Image URL",
        widget=forms.URLInput(attrs={
            'class': 'form-input',
            'placeholder': 'https://example.com/image.jpg'
        })
    )

    class Meta:
        model = Artifact
        fields = ['title', 'category', 'material', 'found_at_site', 'description']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Thracian Golden Rhyton'
            }),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'material': forms.Select(attrs={'class': 'form-select'}),
            'found_at_site': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Panagyurishte, Bulgaria'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 5,
                'placeholder': 'Describe the artifact\'s historical significance...'
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("The title is too short to be descriptive.")
        return title