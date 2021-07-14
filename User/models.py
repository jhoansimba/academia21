from django.contrib.auth.password_validation import password_changed
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    token = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        print(len(self.password))
        if self.pk and len(self.password) != 88:
                self.set_password(self.password)
        if self.pk is None and len(self.password) != 88:
                print('Contraseña: ', self.password)
                self.set_password(self.password)
        return super().save(*args, **kwargs)
