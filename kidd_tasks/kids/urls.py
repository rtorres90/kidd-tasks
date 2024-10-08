from django.urls import path

from . import views

app_name = 'kids'

urlpatterns = [
    path('edit/<int:kid_id>', views.edit_view, name='edit'),
    path('create', views.create_view, name='create'),
    path('list', views.list_view, name='list')
]
