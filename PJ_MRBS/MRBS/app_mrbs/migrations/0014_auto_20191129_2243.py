# Generated by Django 2.2.5 on 2019-11-29 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mrbs', '0013_auto_20191129_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='Timeslot',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='slot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_mrbs.Slot'),
            preserve_default=False,
        ),
    ]