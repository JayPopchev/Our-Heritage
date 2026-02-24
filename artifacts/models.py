from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Artifact(models.Model):
    class MaterialChoices(models.TextChoices):
        GOLD = 'GOLD', 'Gold'
        SILVER = 'SILV', 'Silver'
        BRONZE = 'BRNZ', 'Bronze'
        IRON = 'IRON', 'Iron'
        COPPER = 'COPP', 'Copper'
        LEAD = 'LEAD', 'Lead'

        MARBLE = 'MARB', 'Marble'
        LIMESTONE = 'LIME', 'Limestone'
        FLINT = 'FLNT', 'Flint'
        OBSIDIAN = 'OBSD', 'Obsidian'
        SANDSTONE = 'SAND', 'Sandstone'
        GRANITE = 'GRAN', 'Granite'

        CERAMIC = 'CERA', 'Ceramic'
        GLASS = 'GLAS', 'Glass'
        FAIENCE = 'FAIE', 'Faience'

        BONE = 'BONE', 'Bone'
        WOOD = 'WOOD', 'Wood'
        LEATHER = 'LETH', 'Leather'
        TEXTILE = 'TEXT', 'Textile'
        PAPER = 'PAPR', 'Paper'

        PLASTER = 'PLAS', 'Plaster'
        MIXED = 'MIXD', 'Mixed Materials'
        UNKNOWN = 'UNKN', 'Unknown / Unidentified'

    title = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3)],
    )

    material = models.CharField(
        max_length=10,
        choices=MaterialChoices.choices,
        default=MaterialChoices.UNKNOWN
    )

    found_at_site = models.CharField(
        max_length=150,
    )

    description = models.TextField()

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name='artifacts',
        blank=True
    )

    slug = models.SlugField(unique=True,
                            blank=True,
                            )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

class Exhibition(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    artifacts = models.ManyToManyField('Artifact', related_name='exhibitions')

    def __str__(self):
        return self.title