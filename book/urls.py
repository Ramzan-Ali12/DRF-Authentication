
from django.urls import path
from .views import add
# CRUD urlpatterns
urlpatterns = [
    path('add/', add, name='add'),
    # path('edit/{pk}', edit, name='edit'),
    # path('getAll/', getAll, name='getAll'),
    # path('getById/{pk}',getById,name='getById'),
    # path('delete/{pk}', delete, name='delete'),
]