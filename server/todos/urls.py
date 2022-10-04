from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/<todo_id>", views.delete, name="delete"),
    path("completed/<todo_id>", views.complete, name="completed"),
]
