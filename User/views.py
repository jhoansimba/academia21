from django.contrib.auth.models import Group, User, AbstractUser
from User.forms import FormularioUser
from User.models import *
from django.shortcuts import redirect, render
from django.views.generic import CreateView
# Create your views here.
class addUser(CreateView):
    model = Usuario
    template_name = 'views/user/addUser.html'
    form_class = FormularioUser
    success_url = '/Bienvenido'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupos'] = Group.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        formulario = self.form_class(request.POST)
        try:
            if formulario.is_valid():
                group = formulario.cleaned_data['groups']
                letra = ''
                for i in group:
                    letra = str(i.name)
                username = formulario.cleaned_data['username']
                formulario.cleaned_data['username'] = '{}{}'.format(letra[0], username) 
                formulario.cleaned_data['password'] = '{}{}'.format(letra[0], username) 
                form = FormularioUser(formulario.clean())
                if form.is_valid():
                    form.save()
                    return redirect(self.success_url)
        except Exception as e:
            print('Error Except : ', e)
            return super().post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)