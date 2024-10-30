from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.register_volunteer, name='register'),
    path('', views.volunteer_list, name='volunteer_list'),
]
