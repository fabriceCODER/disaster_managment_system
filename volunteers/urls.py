from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('register/', views.register_volunteer, name='register'),
    path('list/', views.volunteer_list, name='volunteer_list'),
]
