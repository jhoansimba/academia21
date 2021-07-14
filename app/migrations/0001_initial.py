# Generated by Django 3.1.3 on 2021-06-18 18:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_car', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_car', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ciudad', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('i_comp', models.AutoField(primary_key=True, serialize=False)),
                ('file_comp', models.FileField(null=True, upload_to='files/comprobante')),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('imagen_curso', models.ImageField(null=True, upload_to='images/curso', verbose_name='Imagen Curso')),
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direc', models.AutoField(primary_key=True, serialize=False)),
                ('calle1_direc', models.CharField(max_length=50)),
                ('calle2_direc', models.CharField(max_length=50)),
                ('id_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('imagen_est', models.ImageField(null=True, upload_to='images/estudiante')),
                ('id_est', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Cedula')),
                ('nombres_est', models.CharField(max_length=25)),
                ('apellidos_est', models.CharField(max_length=25)),
                ('fecha_est', models.DateField(verbose_name='Fecha Nacimiento')),
                ('email_est', models.EmailField(max_length=254)),
                ('telefono_est', models.CharField(max_length=10)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cursos')),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Ficha_salud',
            fields=[
                ('id_fichsal', models.AutoField(primary_key=True, serialize=False)),
                ('NomEnfer_fichsa', models.CharField(max_length=11, verbose_name='Nombre')),
                ('descripcion_fichsal', models.TextField(verbose_name='Descripción')),
                ('accionesTomar_fichsal', models.TextField(verbose_name='Acciones a tomar')),
                ('telefonoEmer_fichsal', models.CharField(max_length=10, verbose_name='Telefono de emergencia')),
            ],
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id_horario', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_horario', models.TimeField()),
                ('final_horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_provincia', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Talento_Humano',
            fields=[
                ('imagen_th', models.ImageField(null=True, upload_to='images/talento_humano')),
                ('cedula_th', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Cedula')),
                ('nombres_th', models.CharField(max_length=25, verbose_name='Nombres')),
                ('apellidos_th', models.CharField(max_length=25, verbose_name='Apellidos')),
                ('email_est', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefono_est', models.CharField(max_length=10)),
                ('cargo_th', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cargo')),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cursos', verbose_name='Curso')),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.direccion', verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('cedula_rep', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombres_rep', models.CharField(max_length=25)),
                ('apellidos_rep', models.CharField(max_length=25)),
                ('email_est', models.EmailField(max_length=254)),
                ('telefono_est', models.CharField(max_length=10)),
                ('parentezco_rep', models.CharField(max_length=10)),
                ('direccion_rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcial', models.CharField(choices=[('1', 'Uno')], default=1, max_length=1, verbose_name='Parcial')),
                ('p_nota1', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Trabajos')),
                ('p_nota2', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Tareas')),
                ('p_nota3', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='examen')),
                ('parcial2', models.CharField(choices=[('1', 'Dos')], default=1, max_length=1, verbose_name='Parcial')),
                ('s_nota1', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Trabajos')),
                ('s_nota2', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Tareas')),
                ('s_nota3', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='examen')),
                ('parcial3', models.CharField(choices=[('1', 'Tres')], default=1, max_length=1, verbose_name='Parcial')),
                ('t_nota1', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Trabajos')),
                ('t_nota2', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Tareas')),
                ('t_nota3', models.FloatField(null=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='examen')),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cursos', verbose_name='Curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de matrícula')),
                ('matricula', models.BooleanField(default=False)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estudiante')),
                ('id_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comprobante')),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cursos')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='id_fichsal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ficha_salud'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='id_rep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.representante', verbose_name='Nombre del representante'),
        ),
        migrations.AddField(
            model_name='cursos',
            name='id_horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.horarios', verbose_name='Horario'),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='id_est',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estudiante'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='id_provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.provincia'),
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asis', models.AutoField(primary_key=True, serialize=False)),
                ('estado_asis', models.BooleanField()),
                ('fecha_asis', models.DateField(verbose_name='Fecha de asistencia')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estudiante')),
                ('horario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.horarios', verbose_name='Hora')),
            ],
        ),
    ]
