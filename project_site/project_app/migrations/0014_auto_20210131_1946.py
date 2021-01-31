# Generated by Django 3.1.5 on 2021-01-31 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0013_auto_20210131_1927'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='project_employee',
            name='unique assignment',
        ),
        migrations.AddConstraint(
            model_name='project_employee',
            constraint=models.UniqueConstraint(fields=('project', 'employee'), name='unique_project_employee'),
        ),
    ]