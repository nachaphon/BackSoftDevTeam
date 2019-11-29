# Generated by Django 2.2.5 on 2019-11-29 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mrbs', '0014_auto_20191129_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='day',
        ),
        migrations.CreateModel(
            name='RoomDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mrbs.Day')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mrbs.Room')),
            ],
        ),
    ]