from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<str:slug>/', views.view_category, name='view_category'),
    path('<str:slug>/<str:subslug>/', views.view_subcategory, name='view_subcategory'),
]