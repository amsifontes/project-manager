# Generated by Django 2.0.13 on 2019-03-17 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0004_auto_20190316_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='architect_username',
            new_name='architect',
        ),
    ]