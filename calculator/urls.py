from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views
 


urlpatterns=[
    path('',views.calco),
    #path('', views.index, name='indenx'),
    path('visualizza/', views.pagina_dati, name='pagina_dati'),
    path('salva_dati/', views.salva_dati, name='salva_dati'),
]