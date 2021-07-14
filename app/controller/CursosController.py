from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseRedirectBase
from ..models import Cursos, Horarios
from django.db import models
from django.shortcuts import render,HttpResponse

# cursos_model


class Cursos_models():
    def cursos_list():
        cursos = Cursos.objects.order_by('nombre_curso')
        return cursos

    def getcurso(idcurso):
        curso = Cursos.objects.get(id_curso=idcurso)
        return curso
# CursosController


class CursosController():
    def index(request):
       cursos_list = Cursos_models.cursos_list()
       context = {'cursos_list': cursos_list}
       return render(request, 'views/cursos/cursos.html', context)

    def details(request, cursoid):
        object = Cursos_models.getcurso(cursoid)
        context = {'curso': object}
        return render(request, 'views/cursos/details.html', context)

    def obtener_curso(request):
        if request.method=='POST':
            if request.user.is_authenticated:
                 data=request.POST['id_curso']
                 return HttpResponse('<h1>Jhoan Imbaquingo</h1>%s' % data)
            else:
                return HttpResponseRedirect('admin')
# consulta
# def getcursos(idcurso):
#    curso=Cursos.objects.get(id_curso=idcurso)
 #   for item in curso:
  #      Horario=Horarios.objects.get(id_horario=item.id_horario)
