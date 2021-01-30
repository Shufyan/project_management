from django import forms
from .models import Project, Employee, Project_Employee

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        