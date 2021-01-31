from django.core import validators
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models
from django.utils.timezone import now
from django.core.validators import (RegexValidator, MinLengthValidator, MaxLengthValidator)
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from .utils import generate_project_id, generate_employee_id
from datetime import date

# Create your models here.
class Project(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, verbose_name="ID")
    name = models.CharField(blank=False, null=False, max_length=80, validators=[RegexValidator(regex="^(?=.*[a-zA-Z])(?=.*[0-9])[A-Za-z0-9]+$", message="Project name should contain only alphanumeric characters."),
                            MinLengthValidator(10, message="The project name must be of more than 10 characters."),
                            MaxLengthValidator(80, message="The project name must be of less than 80 characters.")])
    description = models.TextField(blank=False, null=False, validators=[
                            MinLengthValidator(50, message="The project description must be of more than 50 characters."),
                            MaxLengthValidator(300, message="The project description must be of less than 300 characters.")])
    start_date = models.DateField(blank=False, null= False, default=now)

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            self.id = generate_project_id() 
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_absolute_url(self):
        return reverse('project_app:project_detail', kwargs={'id': self.id})

class Employee(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=6, verbose_name="ID")
    fullname = models.CharField(blank=False, null=False, max_length=50, validators=[RegexValidator(regex="^[a-zA-Z ]+$", message="Employee name should contain only alphabets."),
                            MinLengthValidator(3, message="The employee name must be of more than 3 characters."),
                            MaxLengthValidator(50, message="The employee name must be of less than 80 characters.")])

    def save(self, *args, **kwargs): 
        if self._state.adding is True:
            self.id = generate_employee_id(6) 
        super(Employee, self).save(*args, **kwargs) 

    def __str__(self):
        return f'{self.id} - {self.fullname}'

    def get_absolute_url(self):
        return reverse('project_app:employee_detail', kwargs={'id': self.id})

class Project_Employee(models.Model):
    project = models.ForeignKey(Project, related_name='projects', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='employees', on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['project','employee'], name='unique_project_employee')]

    def unique_error_message(self, model_class, unique_check):
        if model_class == type(self) and unique_check == ('project', 'employee'):
            return 'This employee is already assigned to this project. Please choose other.'
        else:
            return super(Project_Employee, self).unique_error_message(model_class, unique_check)

    def get_absolute_url(self):
        return reverse('project_app:project_employee_create')
        
    def __str__(self):
        return str(self.pk)

