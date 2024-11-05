from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "users"


def create_groups():
    # Create groups
    Group.objects.get_or_create(name="Admin")
    Group.objects.get_or_create(name="Volunteer")
    Group.objects.get_or_create(name="Regular User")
    Group.objects.get_or_create(name="Administrator")


