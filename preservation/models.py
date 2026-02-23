from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator


class PreservationRecord(models.Model):
    class ConditionChoices(models.TextChoices):
        EXCELLENT = 'EXC', 'Excellent (Stable, no degradation)'
        GOOD = 'GOOD', 'Good (Minor wear, currently stable)'
        FAIR = 'FAIR', 'Fair (Showing signs of deterioration, needs monitoring)'
        POOR = 'POOR', 'Poor (Active degradation, intervention needed)'
        CRITICAL = 'CRIT', 'Critical (Immediate restoration required)'

    artifact = models.ForeignKey(
        'artifacts.Artifact',
        on_delete=models.CASCADE,
        related_name='logs'
    )

    check_date = models.DateField(
        help_text="The date this specific inspection took place."
    )

    condition = models.CharField(
        max_length=4,
        choices=ConditionChoices.choices,
        default=ConditionChoices.GOOD,
    )

    restoration_notes = models.TextField(
        blank=True,
    )

    current_location = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3, message="Location name must be at least 3 characters.")
        ],
    )

    is_on_display = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ['-check_date']