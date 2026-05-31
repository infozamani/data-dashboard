from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataset_list, name='dataset_list'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('api-setup/', views.api_setup, name='api_setup'),
]