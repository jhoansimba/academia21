from xhtml2pdf import pisa
from app.mixin import PermisosUsuario
from django.http.response import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import DeleteView, UpdateView
from app.Formularios.formErtudiante import AddComprobante, AddEstudiante, FormEstudiante
from app.models import Estudiante, Notas, Comprobante
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles import finders
import os
from django.template.loader import get_template
from academia21 import settings

class addComprobante (PermisosUsuario, CreateView):
    permission_required = 'app.add_estudiante'
    model = Comprobante
    form_class = AddComprobante
    template_name = 'views/main.html'
    success_url = '/representante/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Agregar estudiantes'
        context['estudiantes'] = Estudiante.objects.filter(id_rep = self.request.user.pk)
        context['regresar'] = '/representante/'
        return context
class listComprobante(PermisosUsuario, TemplateView):
    permission_required = 'app.view_estudiante'
    model = Comprobante
    template_name = 'views/estudiantes/listadoComprobante.html'
    # template_name = '/estudiantes/'
    title = 'Comprobante'

    def get_context_data(self, **kwargs):
        # est = Estudiante.objects.filter(id_rep = self.request.user.pk)
        # print(est)
        context = super().get_context_data(**kwargs)
        context['name'] = 'Listado de Comprobante'
        context['object_list'] = Estudiante.objects.filter(id_rep = self.request.user.pk)

class listEstudiantes(PermisosUsuario, TemplateView):
    permission_required = 'app.view_estudiante'
    model = Estudiante
    template_name = 'views/estudiantes/listado.html'
    # template_name = '/estudiantes/'
    title = 'Estudiantes'

    def get_context_data(self, **kwargs):
        # est = Estudiante.objects.filter(id_rep = self.request.user.pk)
        # print(est)
        context = super().get_context_data(**kwargs)
        context['name'] = 'Listado de Estudiantes'
        context['object_list'] = Estudiante.objects.filter(id_rep = self.request.user.pk)
        return context
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,  *args, **kwargs)
    def post(self, request,  *args, **kwargs):
        data = {}
        try:
            id = request.POST['id']
            print('ID estudiante : ', id)
            data = Notas.objects.get(estudiante_id = id).json()

        except:
            data = {'error':'Estudiante sin Notas'}
        return JsonResponse(data, safe=False)

class addEstudiuantes(PermisosUsuario, CreateView):
    permission_required = 'app.add_estudiante'
    model = Estudiante
    form_class = AddEstudiante
    template_name = 'views/estudiantes/addEstudiante.html'
    success_url = '/representante/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Agregar estudiantes'
        context['regresar'] = '/representante/'
        return context
class editEstudiuantes(PermisosUsuario, UpdateView):
    permission_required = 'app.change_estudiante'
    model = Estudiante
    form_class = FormEstudiante
    template_name = 'views/estudiantes/addEstudiante.html'
    success_url = '/representante/'
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance = self.get_object())
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Actualizar estudiante'
        context['regresar'] = '/representante/'
        return context
class deleteEstudiuantes(PermisosUsuario, DeleteView):
    permission_required = 'app.delete_estudiante'
    model = Estudiante
    form_class = FormEstudiante 
    template_name = 'views/main.html'
    success_url = '/representante/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Eliminar estudiantes'
        context['regresar'] = '/estudiantes/'
        context['info'] = kwargs
        return context
class Comprobante (View):
    def link_callback(self, uri, rel):
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="Comprobante.pdf"'
        template = get_template('views/estudiantes/comprobante.html')
        est = Estudiante.objects.get(id_est = id)
        data = {
            'est' : est, 
            'title' : f'Comprobante a pagar de {est.Estudiante()}'
        }
        html = template.render(data)
         # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response,
        link_callback=self.link_callback
        )
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

        # return JsonResponse(data, safe=False)