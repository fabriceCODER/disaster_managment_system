# volunteers/models.py
from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Allows null values
    skills = models.TextField(help_text="List skills separated by commas")

    def __str__(self):
        return self.name
