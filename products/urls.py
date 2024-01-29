from django.urls import path
from .views import add, edit, getAll, delete

urlpatterns = [
    path("add/", add, name="add"),
    path("edit/<int:pk>/", edit, name="edit"),
    path("getAll/", getAll, name="getAll"),
    path("delete/<int:pk>/", delete, name="delete"),
]
