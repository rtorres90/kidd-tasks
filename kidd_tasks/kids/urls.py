from django.urls import path

from . import views

app_name = 'kids'

urlpatterns = [
    path('create', views.create_view, name='create')
]
