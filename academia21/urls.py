"""academia21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls.conf import include
from app.controller.AsistenciaController import AddAsistencia, Asistencialist
from django.contrib import admin
from django.urls import path
from app.controller.indexController import indexController
from django.conf import settings
from django.conf.urls.static import static
from app.controller.CursosController import CursosController
from app.controller.UserController import UserController
from app.controller.nosotrosController import nosotrosController

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', indexController.index, name='index'),
    path('nosotros/', nosotrosController.index, name='nosotros'),
    path('admin/', admin.site.urls, name='login'),
    path('asistencia/', Asistencialist, name='asistencia'),
    path('asistencia/add', AddAsistencia.as_view(), name='add_asistencia'),
    path('cursos/', CursosController.index, name='cursos'),
    path('details/<int:cursoid>', CursosController.details, name='details'),
    path('', include('User.urls')),
    # path('Registrar', CursosController.obtener_curso, name='Registrar'),
    # path('report/<int:')
    path('register/', UserController.register, name='register')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
