from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('manual/<int:id>/', views.manual, name='manual'),
    
]