# Generated by Django 3.1.5 on 2021-01-30 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0009_auto_20210131_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='A7rjKZ', editable=False, max_length=6, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(default=407, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
