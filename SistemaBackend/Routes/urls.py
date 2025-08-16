from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('registro/', views.registro, name="registrar"),
    path('administracion/', views.administracion, name="administracion"),
]