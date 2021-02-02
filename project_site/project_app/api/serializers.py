from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from project_app.models import Project, Employee, Project_Employee

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

class Project_EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project_Employee
        fields = "__all__"

        validators = [
            UniqueTogetherValidator(
                queryset=Project_Employee.objects.all(),
                fields=['project', 'employee']
            )
        ]