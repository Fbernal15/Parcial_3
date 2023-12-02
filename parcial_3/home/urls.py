from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('index/', views.index, name='index'),
    path('nueva/', views.crearNota, name='nueva'),
    path('borrarNota/<id>/',views.borrarNota, name='borrarNota'),
    path('editarNota/<id>/', views.editarNota, name='editarNota'),
    path('verNota/<id>/', views.verNota, name='verNota'),
    path('registro/',views.registro,name='registro')
    
      
]