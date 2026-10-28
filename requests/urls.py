from django.urls import path
from .views import (
    create_request,
    request_list,
    apply_to_request,
    complete_request,
    confirm_request,
    edit_request,
)

urlpatterns = [
    path("", request_list, name="request_list"),
    path("create/", create_request, name="request_create"),
    path("<int:request_id>/apply/", apply_to_request, name="request_apply"),
    path("<int:request_id>/complete/", complete_request, name="request_complete"),
    path("<int:request_id>/confirm/", confirm_request, name="request_confirm"),
    path("<int:request_id>/edit/", edit_request, name="request_edit"),
]