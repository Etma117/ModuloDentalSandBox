# Generated by Django 4.2 on 2024-02-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinicas', '0001_initial'),
        ('schedule', '0014_use_autofields_for_pk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.event')),
            ],
            bases=('schedule.event',),
        ),
        migrations.CreateModel(
            name='CitasDentalesCalendar',
            fields=[
                ('calendar_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.calendar')),
            ],
            bases=('schedule.calendar',),
        ),
        migrations.CreateModel(
            name='DentistaCalendar',
            fields=[
                ('calendar_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.calendar')),
            ],
            bases=('schedule.calendar',),
        ),
        migrations.CreateModel(
            name='DiasNoLaborablesCalendar',
            fields=[
                ('calendar_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.calendar')),
                ('clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinica_agenda_nolabor', to='clinicas.clinica')),
            ],
            bases=('schedule.calendar',),
        ),
    ]
