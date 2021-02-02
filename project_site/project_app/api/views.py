from project_app.models import Project, Employee, Project_Employee
from .serializers import ProjectSerializer, EmployeeSerializer, Project_EmployeeSerializer
from rest_framework import generics

# Project API View
class ApiProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ApiProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ApiProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ApiProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ApiProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Employee API View
class ApiEmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ApiEmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ApiEmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ApiEmployeeUpdateView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ApiEmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Project_Employee API View
class ApiProject_EmployeeCreateView(generics.CreateAPIView):
    queryset = Project_Employee.objects.all()
    serializer_class = Project_EmployeeSerializer

class ApiProject_EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Project_Employee.objects.all()
    serializer_class = Project_EmployeeSerializer