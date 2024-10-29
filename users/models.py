from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "users"
