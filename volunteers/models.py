from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    skills = models.TextField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null= True)

    def __str__(self):
        return self.name
