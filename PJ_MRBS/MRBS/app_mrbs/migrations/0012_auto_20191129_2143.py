# Generated by Django 2.2.5 on 2019-11-29 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mrbs', '0011_auto_20191129_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeslot',
            old_name='toslot',
            new_name='slot',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_mrbs.Room'),
            preserve_default=False,
        ),
    ]
