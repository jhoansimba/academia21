from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView

# Create your views here.
class Login(LoginView):
    template_name = 'login.html'
    