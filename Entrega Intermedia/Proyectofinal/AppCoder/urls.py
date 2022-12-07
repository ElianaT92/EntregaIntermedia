from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('cursosApi/', views.cursosapi),
    path('profesoresApi/', views.profesoresapi),
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name='Profesores'),
    path('egresados/', views.egresados, name='Egresados'),
    path('busquedaCurso/', views.buscarcurso),
    path('busquedaProfesor/', views.buscarprofesor),
    path('buscar/', views.buscar),
    path('buscarprofe/',views.buscarprofe),
    path('busquedaEgresado/', views.buscaregresado),
    path('buscaregreso/', views.buscaregreso),
    

]