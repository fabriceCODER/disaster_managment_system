from django.db import models
from django.core.validators import MinValueValidator
from resourses.models import Resource


class Disaster(models.Model):
    DISASTER_TYPES = [
        ('flood', 'Flood'),
        ('earthquake', 'Earthquake'),
        ('fire', 'Fire'),
        ('storm', 'Storm'),
        ('drought', 'Drought'),
        ('landslide', 'Landslide'),
        ('tsunami', 'Tsunami'),
        ('volcano', 'Volcano'),
    ]

    SEVERITY_CHOICES = [
        (1, 'Low'),
        (2, 'Moderate'),
        (3, 'High'),
        (4, 'Severe'),
        (5, 'Critical'),
    ]

    # Basic Information
    disaster_id = models.AutoField(primary_key=True)  # Unique ID for the disaster record
    type = models.CharField(max_length=50, choices=DISASTER_TYPES)  # Type of disaster
    location = models.CharField(max_length=100)  # Location of the disaster
    date = models.DateField()  # Date of the disaster
    severity = models.IntegerField(choices=SEVERITY_CHOICES,
                                   validators=[MinValueValidator(1)])  # Severity rating from 1 to 5
    response = models.TextField()  # Response actions taken

    # Additional Information
    reported_by = models.CharField(max_length=50)  # Who reported the disaster
    status = models.CharField(max_length=20, default='active')  # Current status of the disaster

    class Meta:
        db_table = "disasters"  # Force the naming of the table
        verbose_name_plural = "Disasters"  # Human-readable name for the plural form

        # # Link to Resource model (many-to-many, as a disaster might need multiple resources)
        # resources_needed = models.ManyToManyField(Resource, related_name="disasters", blank=True)

    def __str__(self):
        return f"{self.type} in {self.location} on {self.date}"

    class Meta:
        db_table = "disasters"
