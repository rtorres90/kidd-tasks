from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('edit/<int:task_id>', views.edit_view, name='edit'),
    path('create', views.create_view, name='create'),
    path('list', views.list_view, name='list')
]
