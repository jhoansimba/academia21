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
    success_url = '/admin/login/'
    def post(self, request, *args, **kwargs):
        formulario = self.form_class(request.POST)
        if formulario.is_valid():
            p = formulario.clean()
            print(p)

            formulario.save()
            return redirect(self.success_url)
        #     groups = formulario.cleaned_data['groups']
        #     password = formulario.cleaned_data.get('password')
        #     username = formulario.cleaned_data.get('username')
        #     first_name = formulario.cleaned_data.get('first_name')
        #     last_name = formulario.cleaned_data.get('last_name')
        #     email = formulario.cleaned_data.get('email')
        #     user = User.objects.create_user(username=username,
        #                                 first_name=first_name,
        #                                 last_name=last_name,
        #                                 email=email,
        #                                 password=password,
        #                                 is_staff=1)
        #     for i in groups:
        #        g = Group.objects.get(name = i)
        #        user.groups.add(g)
        #        user.save()
        # return redirect(self.success_url)

    