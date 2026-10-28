from django.urls import path

from .views import partner_dashboard


urlpatterns = [
    path("dashboard/", partner_dashboard, name="partner_dashboard"),
]