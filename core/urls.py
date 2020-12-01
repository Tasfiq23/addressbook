from django.urls import path
from . import views
from .views import list_persons, new_person, delete_person

app_name = 'core'

urlpatterns = [
    path('new/', new_person, name='new'),
    path('delete/<int:id>/', delete_person, name='delete'),
    path('', list_persons, name='index')
]
