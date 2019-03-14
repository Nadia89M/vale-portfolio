from django.urls import path
from . import views

urlpatterns = [
    path('<str:slug>', views.view_category, name='view_category'),
]