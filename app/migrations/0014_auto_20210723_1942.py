# Generated by Django 3.1.3 on 2021-07-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210723_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talento_humano',
            name='id_curso',
        ),
        migrations.AddField(
            model_name='talento_humano',
            name='id_curso',
            field=models.ManyToManyField(to='app.Cursos', verbose_name='Curso'),
        ),
    ]
