from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import contact

urlpatterns = [
    path('', contact, name='contact'),
    path('success/', views.success, name='success'),

]
