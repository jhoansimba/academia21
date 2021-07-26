from django.contrib.auth.password_validation import password_changed
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
#     opciones = [
#             ('1', 'Asistente'),
#             ('2', 'Docente'),
#             ('3', 'Representante'),
#             ]
    token = models.CharField(max_length=50, blank=True, null=True)
#     rol = models.CharField(max_length=2, choices=opciones, blank=True, null=True)

    def save(self, *args, **kwargs):
        print(len(self.password))
        if self.pk and len(self.password) != 88:
                self.set_password(self.password)
        if self.pk is None:
                pw = str(self.password)
                cont = '_sha256$'
                if pw.count(cont) == 0:
                        print('Entró ,', self.password)
                        self.set_password(self.password)
        return super().save(*args, **kwargs)
