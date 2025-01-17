# Generated by Django 4.2 on 2024-02-29 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_customuser_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistente',
            name='user',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='user',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='user',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tipo_usuario',
            field=models.CharField(choices=[('administrador', 'Administrador'), ('dentista', 'Dentista'), ('asistente', 'Asistente'), ('paciente', 'Paciente'), ('responsable', 'Responsable')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='Asistente',
        ),
        migrations.DeleteModel(
            name='Medico',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
    ]
