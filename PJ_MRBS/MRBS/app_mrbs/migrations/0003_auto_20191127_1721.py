# Generated by Django 2.2.5 on 2019-11-27 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mrbs', '0002_account_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_name',
            new_name='username',
        ),
    ]
