from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo, name="todo"),
    path("enter/", views.enter, name="enter"),
    path("register/", views.create_account, name="register"),
    path("exit/", views.exit, name="exit"),
    path("edit/<int:task_id>/", views.edit, name="edit"),
    path("delete/<int:task_id>/", views.delete, name="delete"),

]

