# Generated by Django 3.1.5 on 2021-01-31 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0014_auto_20210131_1946'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='project_employee',
            name='unique_project_employee',
        ),
    ]