# Generated by Django 2.2.5 on 2019-11-29 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mrbs', '0012_auto_20191129_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='slot',
        ),
        migrations.AddField(
            model_name='slot',
            name='Timeslot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_mrbs.Timeslot'),
            preserve_default=False,
        ),
    ]
