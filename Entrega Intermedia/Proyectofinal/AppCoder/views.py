from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.models import Profesores
from AppCoder.models import Egresados
from django.core import serializers
from AppCoder.forms import CursoFormulario
from AppCoder.forms import ProfesorFormulario
from AppCoder.forms import EgresadosFormulario

# Create your views here.
def cursos(request):

    if request.method == "POST":
	    
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                curso.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()	
    
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


def profesores(request):

    if request.method == "POST":
	    
            profeFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
            print(profeFormulario)

            if profeFormulario.is_valid:
                resultado = profeFormulario.cleaned_data
                profesores = Profesores(profesor=resultado["profesor"], asignatura=resultado["asignatura"])
                profesores.save()
                return render(request, "AppCoder/inicio.html")
    else:
        profeFormulario = ProfesorFormulario()	
    
    return render(request, "AppCoder/profesores.html", {"profeFormulario": profeFormulario})

def egresados(request):

    if request.method == "POST":
	    
            egresoFormulario = EgresadosFormulario(request.POST) # Aqui me llega la informacion del html
            print(egresoFormulario)

            if egresoFormulario.is_valid:
                resultadoegresados = egresoFormulario.cleaned_data
                egresados = Egresados(nombre=resultadoegresados["egresado"], titulacion=resultadoegresados["titulacion"])
                egresados.save()
                return render(request, "AppCoder/inicio.html")
    else:
        egresoFormulario = EgresadosFormulario()	
    
    return render(request, "AppCoder/egresados.html", {"egresoFormulario": egresoFormulario})

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursosapi(request):
    cursos_todos=Curso.objects.all()
    return HttpResponse (serializers.serialize('json',cursos_todos))

def profesoresapi(request):
    profesores_todos=Profesores.objects.all()
    return HttpResponse (serializers.serialize('json',profesores_todos))

def buscarcurso(request):
    return render(request, 'AppCoder/busquedaCurso.html')

def buscar(request):
    camada_views= request.GET['camada']
    cursos_todos=Curso.objects.filter(camada=camada_views)
    return render(request, 'AppCoder/resultadoCurso.html',{'camada':camada_views,'cursos':cursos_todos})

def buscarprofesor(request):
    return render(request, 'AppCoder/busquedaProfesor.html')

def buscarprofe(request):
    asignatura_views= request.GET['asignatura']
    profesores_todos=Profesores.objects.filter(asignatura=asignatura_views)
    return render(request, 'AppCoder/resultadoProfesor.html',{'asignatura':asignatura_views,'profesores':profesores_todos})

def buscaregreso(request):
    titulacion_views= request.GET['titulacion']
    egresados_todos=Egresados.objects.filter(titulacion=titulacion_views)
    return render(request, 'AppCoder/resultadoEgresado.html',{'titulacion':titulacion_views,'egresados':egresados_todos})

def buscaregresado(request):
    return render(request, 'AppCoder/busquedaEgresado.html')