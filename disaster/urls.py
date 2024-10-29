from django.urls import path
from . import views

urlpatterns = [
    path("", views.disaster_list, name="disaster_list"),  # List of disasters
    path("create/", views.create_disaster, name="create_disaster"),  # Create a new disaster record
    path("update/<pk>/", views.update_disaster, name="update_disaster"),  # Update an existing disaster record
    path("delete/<pk>/", views.delete_disaster, name="delete_disaster"),  # Delete a disaster record
]
