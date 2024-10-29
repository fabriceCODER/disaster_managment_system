from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("resources", views.resource_list, name="resource_list"),
    path("resources/create/", views.create_resource, name="create_resource"),
    path("update/<int:pk>/", views.update_resource, name="update_resource"),
    path("delete/<int:pk>/", views.delete_resource, name="delete_resource"),
]

