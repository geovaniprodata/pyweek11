from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
     path('logar/', views.logar, name='logar'),
]
