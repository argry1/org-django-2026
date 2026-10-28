from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("requests/", include("requests.urls")),
    path("rewards/", include("rewards.urls")),
    path("partners/", include("partners.urls")),
]