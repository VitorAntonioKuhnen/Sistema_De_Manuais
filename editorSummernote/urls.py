from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('manual/<int:id>/', views.manual, name='manual'),
    path('btAdicionar/', views.btAdicionar, name='btAdicionar'),
    path('adicionar_manual/', views.adicionar_manual, name='adicionar_manual'),
    
]