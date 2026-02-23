from django.db import models

# Create your models here.
class Category(models.Model):
    class BulgarianEra(models.TextChoices):
        PREHISTORIC = 'PRE', 'Prehistoric'
        THRACIAN = 'THRA', 'Thracian Period'
        ROMAN = 'ROMN', 'Roman & Late Antiquity'
        FIRST_EMP = 'EMP1', 'First Bulgarian Empire (681–1018)'
        BYZANTINE = 'BYZ', 'Byzantine Period'
        SECOND_EMP = 'EMP2', 'Second Bulgarian Empire (1185–1396)'
        OTTOMAN = 'OTTM', 'Ottoman Period'
        MODERN = 'MODR', 'Modern/Recent (Post-1878)'

    name = models.CharField(
        max_length=4,
        choices=BulgarianEra.choices,
        help_text="Select the historical era."
    )
    description = models.TextField(
        blank=True
    )



