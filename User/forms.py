from User.models import Usuario
from django.db import models
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.models import AbstractUser, User
class FormularioUser(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['autofocus'] = True
        # self.fields['is_superuser'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_staff'].widget.attrs['class'] = 'form-check-input'
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'password', 'groups', 'is_staff')
        widgets = {
            'password' : widgets.PasswordInput()
        }