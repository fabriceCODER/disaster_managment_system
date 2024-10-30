from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    availability = models.CharField(max_length=50)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.name
