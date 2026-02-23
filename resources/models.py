from django.db import models

# Create your models here.
class ArtifactResource(models.Model):
    artifact = models.ForeignKey('artifacts.Artifact',
                                 on_delete=models.CASCADE,
                                 related_name='media',
                                 )
    description = models.CharField(
        max_length=255,
        blank=True,
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )