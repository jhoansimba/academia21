from django.forms.models import model_to_dict
from django.utils.html import format_html
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.enums import ChoicesMeta

class Provincia (models.Model):
    id_provincia=models.AutoField(primary_key=True)
    nombre_provincia=models.CharField(max_length=11)

class Ciudad (models.Model):
    id_ciudad=models.AutoField(primary_key=True)
    nombre_ciudad=models.CharField(max_length=11)
    id_provincia=models.ForeignKey(Provincia,on_delete=models.CASCADE)

class Direccion (models.Model):
    id_direc=models.AutoField(primary_key=True)
    calle1_direc=models.CharField(max_length=50)
    calle2_direc=models.CharField(max_length=50)
    id_ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    def Direccion (self):
        txt = '{0}{1}{2}'
        return txt.format(self.calle1_direc," y ",self.calle2_direc)

    def __str__(self) -> str:
        txt = '{0}{1}{2}'
        return txt.format(self.calle1_direc," y ",self.calle2_direc)

class Representante (models.Model):

    
    cedula_rep=models.CharField(max_length=10, primary_key=True)
    nombres_rep=models.CharField(max_length=25)
    apellidos_rep=models.CharField(max_length=25)
    direccion_rep=models.ForeignKey(Direccion, on_delete=CASCADE)
    email_est=models.EmailField()
    telefono_est=models.CharField(max_length=10)
    parentezco_rep=models.CharField(max_length=10)
    def Representante (self):
        txt = '{0} {1} '
        return txt.format(self.nombres_rep, self.apellidos_rep)
    def __str__(self) -> str:
        txt = '{0} {1} '
        return  txt.format(self.nombres_rep,self.apellidos_rep)





class Horarios (models.Model):
    id_horario=models.AutoField(primary_key=True)
    inicio_horario=models.TimeField()
    final_horario=models.TimeField()
    def Horario (self):
        txt = '{0}{1}{2}'
        return txt.format(self.inicio_horario," a ", self.final_horario )
    def __str__(self) -> str:
        txt = '{0}{1}{2}'
        return txt.format(self.inicio_horario," a ", self.final_horario )
        
class Cursos (models.Model):
    imagen_curso=models.ImageField(null=True,upload_to='images/curso',verbose_name="Imagen Curso")
    id_curso=models.AutoField(primary_key=True)
    nombre_curso=models.CharField(max_length=25)
    id_horario=models.ForeignKey(Horarios,on_delete=models.CASCADE ,verbose_name="Horario")
    def Cursos (self):
        txt = '{0}'
        return txt.format(self.nombre_curso)
    def __str__(self) -> str:
        txt = '{0}'
        return txt.format(self.nombre_curso )
    def Horario (self):
        txt = '{0} {1} {2} '
        return txt.format(self.horarios.inicio_horario," a ", self.horarios.final_horario )
    def json(self):
        datos = model_to_dict(self)
        return datos

class  Estudiante(models.Model):
    # id_est=models.AutoField(primary_key=True)
    imagen_est=models.ImageField(null=True,upload_to='images/estudiante')
    id_est=models.CharField(max_length=10, primary_key=True, verbose_name= 'Cedula')
    nombres_est=models.CharField(max_length=25)
    apellidos_est=models.CharField(max_length=25)
    #edad_est=models.DateField()
    fecha_est=models.DateField(verbose_name='Fecha Nacimiento')
    email_est=models.EmailField()
    telefono_est=models.CharField(max_length=10)
    id_rep=models.CharField(max_length=3, null=True, blank=True)
   # id_fichsal=models.ForeignKey(Ficha_salud,on_delete=models.CASCADE)
    id_curso=models.ForeignKey(Cursos,on_delete=models.CASCADE)
    id_direccion=models.ForeignKey(Direccion,on_delete=models.CASCADE)

    
    

    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.nombres_est, self.apellidos_est)

    def __str__(self) -> str:
        txt = '{0} {1} '
        return  txt.format(self.nombres_est,self.apellidos_est)
    def Representante (self):
        txt = '{0} {1} '
        return txt.format(self.representante.nombres_rep, self.representante.apellidos_rep)
    def Salud (self):
        txt = '{0} '
        return txt.format(self.salud.NomEnfer_fichsa)
    def Cursos (self):
        txt = '{0}'
        return txt.format(self.cursos.nombre_curso)
    def Direccion (self):
        txt = '{0}{1}{2}'
        return txt.format(self.direccion.calle1_direc," y ",self.direccion.calle2_direc)

class Ficha_salud (models.Model):
    id_est = models.ForeignKey(Estudiante, on_delete=CASCADE)
    id_fichsal=models.AutoField(primary_key=True)
    NomEnfer_fichsa=models.CharField(max_length=11, verbose_name='Nombre')
    descripcion_fichsal=models.TextField(verbose_name='Descripción')
    accionesTomar_fichsal=models.TextField(verbose_name='Acciones a tomar')
    telefonoEmer_fichsal=models.CharField(max_length=10, verbose_name='Telefono de emergencia')
   
    def Salud (self):
        txt = '{0}'
        return txt.format(self.NomEnfer_fichsa)
    def __str__(self) -> str:
        txt = '{0}'
        return txt.format(self.NomEnfer_fichsa)
    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.Estudiante.nombres_est, self.Estudiante.apellidos_est)

class Cargo (models.Model):
    id_car=models.AutoField(primary_key=True)
    nombre_car=models.CharField(max_length=15)
    def Cargo (self):
        txt = '{0}'
        return txt.format(self.nombre_car)

    def __str__(self) -> str:
        txt = '{0}'
        return txt.format(self.nombre_car)
class Talento_Humano (models.Model):
   
   
    imagen_th=models.ImageField(null=True,upload_to='images/talento_humano')
    cedula_th=models.CharField(max_length=10, primary_key=True,verbose_name='Cedula')
    nombres_th=models.CharField(max_length=25, verbose_name='Nombres')
    apellidos_th=models.CharField(max_length=25, verbose_name='Apellidos')
    cargo_th=models.ForeignKey(Cargo, on_delete=models.CASCADE)
    email_est=models.EmailField(verbose_name='E-mail')
    telefono_est=models.CharField(max_length=10)
    id_curso=models.ManyToManyField(Cursos,verbose_name='Curso')
    id_direccion=models.ForeignKey(Direccion, on_delete=models.CASCADE, verbose_name='Dirección')
    def Talento_Humano(self):
        txt = '{0} {1} '
        return txt.format(self.nombres_th, self.apellidos_th)
    def __str__(self) -> str:
        txt = '{0} {1} '
        return txt.format(self.nombres_th, self.apellidos_th)
    def Cargo (self):
        txt = '{0}'
        return txt.format(self.Cargo.nombre_car)


class Notas (models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=CASCADE)
    curso_id= models.ForeignKey(Cursos, on_delete=CASCADE, verbose_name='Curso')
    parcial = models.CharField(choices=[('1','Uno')], default=1, max_length=1, verbose_name='Parcial')
    p_nota1 = models.FloatField(verbose_name='Trabajos',null=1, validators=[MaxValueValidator(10),MinValueValidator(0)])
    p_nota2 = models.FloatField(verbose_name='Tareas', null=1,validators=[MaxValueValidator(10),MinValueValidator(0)])
    p_nota3 = models.FloatField(verbose_name='examen',null=1, validators=[MaxValueValidator(10),MinValueValidator(0)])
    
    parcial2 = models.CharField(choices=[('1','Dos')], default=1, max_length=1, verbose_name='Parcial')
    s_nota1 = models.FloatField(verbose_name='Trabajos',null=1, validators=[MaxValueValidator(10),MinValueValidator(0)])
    s_nota2 = models.FloatField(verbose_name='Tareas', null=1,validators=[MaxValueValidator(10),MinValueValidator(0)])
    s_nota3 = models.FloatField(verbose_name='examen',null=1, validators=[MaxValueValidator(10),MinValueValidator(0)])
    parcial3 = models.CharField(choices=[('1','Tres')], default=1, max_length=1, verbose_name='Parcial')
    t_nota1 = models.FloatField(verbose_name='Trabajos',null=1, validators=[MaxValueValidator(10),MinValueValidator(0)])
    t_nota2 = models.FloatField(verbose_name='Tareas',null=1, validators=[MaxValueValidator(10),MinValueValidator(0)])
    t_nota3 = models.FloatField(verbose_name='examen', null=1,validators=[MaxValueValidator(10),MinValueValidator(0)])
    sumatoria = models.FloatField(editable=False)
    promedio = models.FloatField(editable=False)
    estado = models.BooleanField(editable=False)
    def save(self, *args, **kwargs):
        self.sumatoria = self.SumaGeneral()
        self.promedio = self.Promedio()
        self.estado = self.EstadoEst()
        return super(Notas, self).save(*args, **kwargs)
    def json(self):
        datos = model_to_dict(self)
        datos['suma'] = self.SumaGeneral()
        datos['promedio'] = self.Promedio()
        datos['estado'] = self.EstadoEst()
        datos['curso_id'] = self.curso_id.Cursos()
        datos['est'] = self.Estudiante()
        return datos
    def SumaParcialUno(self):
        suma = (self.p_nota1 + self.p_nota2 +self.p_nota3) / 3
        return round((suma), 2)
    def SumaParcialDos(self):
        suma = (self.s_nota1 + self.s_nota2 +self.s_nota3) / 3
        return round((suma), 2)
    def SumaParcialTres(self):
        suma = (self.t_nota1 + self.t_nota2 +self.t_nota3) / 3
        return round((suma), 2)
    def SumaGeneral(self):
        uno = Notas.SumaParcialUno(self)
        dos = Notas.SumaParcialDos(self)
        tres = Notas.SumaParcialTres(self)
        suma = uno + dos + tres
        return round(suma, 2)
    def Promedio(self):
        promedio = Notas.SumaGeneral(self) / 3
        return round(promedio,2)
    def Estado(self):
        if Notas.SumaGeneral(self) > 20.5:
            return format_html("<spam style='color: green;' > Aprobado </spam>")
        else:
            return format_html("<spam style='color: red;' > Reprobado </spam>")
    def EstadoEst(self):
        if Notas.SumaGeneral(self) > 20.5:
            return True
        else:
            return False
    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.estudiante.nombres_est, self.estudiante.apellidos_est)
    def Cursos (self):
        txt = '{0}'
        return txt.format(self.curso_id.nombre_curso)
class Comprobante (models.Model):
    i_comp= models.AutoField(primary_key=True)
    id_est=models.ForeignKey(Estudiante, on_delete=CASCADE)
    file_comp=models.FileField(null=True,upload_to='files/comprobante')
    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.Estudiante.nombres_est, self.Estudiante.apellidos_est)
    def comp (self):
        txt='{0}{1}'
        return txt.format("comprobante de: ",self.id_est)
    def __str__(self) -> str:
        txt='{0}{1}'
        return txt.format("comprobante de: ",self.id_est)
   
class Matricula(models.Model):
    
    fecha = models.DateField(verbose_name='Fecha de matrícula')
    estudiante = models.ForeignKey(Estudiante, on_delete=CASCADE)
    id_comp=models.ForeignKey(Comprobante, on_delete=CASCADE)
    id_curso= models.ForeignKey(Cursos, on_delete=CASCADE)
    matricula=models.BooleanField(default=False)
    

    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.estudiante.nombres_est, self.estudiante.apellidos_est)
    #def comp (self):
     #   txt='{0}{1}{2}'
      #  return txt.format("comprobante de:",self.comprobante.i_comp,self.comprobante.file_comp)
    
class Asistencia (models.Model):
    estudiante = models.ManyToManyField(Estudiante)
    id_asis=models.AutoField(primary_key=True)
    estado_asis=models.BooleanField()
    fecha_asis=models.DateField(verbose_name='Fecha de asistencia')
    horario_id= models.ForeignKey(Horarios, on_delete=CASCADE, verbose_name='Hora')
    def Estudiante(self) -> str:
        txt = ''
        for i in self.estudiante.all():
            txt += i.nombres_est
        return txt




    
    