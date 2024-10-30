from django.urls import path
from django.views.generic import TemplateView

from .views import contact_view

urlpatterns = [
    path('', contact_view, name='contact'),  # URL for the contact page
    path('success/', TemplateView.as_view(template_name='contact/success.html'), name='contact_success'),  # Success page
]
