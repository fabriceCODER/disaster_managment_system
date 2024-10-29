from django.db import models


class Resource(models.Model):
    RESOURCE_TYPES = [
        ("medical", "Medical"),
        ("food", "Food"),
        ("shelter", "Shelter"),
        ("clothing", "Clothing"),
        ("transport", "Transport"),
        ("volunteers", "Volunteers"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=RESOURCE_TYPES)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=150)
    availability_status = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.type}"

    class Meta:
        db_table = "resources"
