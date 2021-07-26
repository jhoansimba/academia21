from django.utils.html import format_html
from app.models import Asistencia, Cargo, Ciudad, Comprobante, Cursos, Direccion, Estudiante, Ficha_salud, Horarios, Matricula, Notas, Provincia, Representante, Talento_Humano
from django.contrib import admin


# Register your models here.

@admin.register(Notas)
class Notas(admin.ModelAdmin):
    list_display = ('Estudiante','curso_id','SumaParcialUno','SumaParcialDos','SumaParcialTres','SumaGeneral','Promedio','Estado')

@admin.register(Asistencia)
class Asistencia(admin.ModelAdmin):
    list_display = ('Estudiante','fecha_asis','estado_asis')
    search_fields = ('fecha_asis','estado_asis')
    list_filter = ('estado_asis',)

@admin.register(Representante)
class Representante (admin.ModelAdmin):
    list_display=('Representante', 'cedula_rep', 'telefono_est', 'parentezco_rep')



@admin.register(Estudiante)
class Estudiante(admin.ModelAdmin):
    list_display = ('Estudiante','id_est','telefono_est', 'Fotografia')

    def Fotografia(self, obj):
        return format_html("<img src={0} width='100' height='100' > ".format(obj.imagen_est.url))

admin.site.register(Ciudad )
admin.site.register(Direccion)
admin.site.register(Provincia)
@admin.register(Cursos)
class Cursos(admin.ModelAdmin):
     list_display=('nombre_curso','id_horario','Fotografia_Curso')
     def Fotografia_Curso(self, obj):
        return format_html("<img src={0} width='100' height='100' > ".format(obj.imagen_curso.url,))

@admin.register(Matricula)
class Estudiante (admin.ModelAdmin):
    list_display=('Estudiante','fecha', 'matricula')


admin.site.register(Horarios)

@admin.register(Ficha_salud)
class Ficha_salud (admin.ModelAdmin):
    list_display=('id_est', 'Salud', 'descripcion_fichsal', 'accionesTomar_fichsal', 'telefonoEmer_fichsal')

admin.site.register(Talento_Humano)
admin.site.register(Cargo)

@ admin.register(Comprobante)
class Comprobante (admin.ModelAdmin):
    list_display=('Comprobante_sellado', 'id_est')
    def Comprobante_sellado(self, obj):
        return format_html("<h5> {0} </h5> ".format(obj.file_comp,))


# admin.site.register(Aul)

