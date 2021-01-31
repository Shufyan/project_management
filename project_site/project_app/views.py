from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Project, Employee, Project_Employee
from .forms import ProjectForm, EmployeeForm, Project_EmployeeForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    context_object_name = "home"

# Project Views
class ProjectListView(ListView):
    context_object_name = "projects"
    model = Project

class ProjectDetailView(DetailView):
    context_object_name = "project_detail"
    model = Project
    template_name = "project_app/project_detail.html"

class ProjectCreateView(CreateView):
    form_class = ProjectForm
    model = Project
    template_name = 'project_app/project_form.html'
    success_url = reverse_lazy('project_app:project_list')    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            print('ERROR FORM INVALID')
            return render(request, self.template_name, {'form': form})

class ProjectUpdateView(UpdateView):
    form_class = ProjectForm
    model = Project
    template_name = 'project_app/project_form.html'
    success_url = reverse_lazy('project_app:project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project_app:project_list')

# Employee Views
class EmployeeListView(ListView):
    context_object_name = "employees"
    model = Employee

class EmployeeDetailView(DetailView):
    context_object_name = "employee_detail"
    model = Employee
    template_name = "project_app/employee_detail.html"

class EmployeeCreateView(CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'project_app/employee_form.html'
    success_url = reverse_lazy('project_app:employee_list')    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            print('ERROR FORM INVALID')
            return render(request, self.template_name, {'form': form})

class EmployeeUpdateView(UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'project_app/employee_form.html'
    success_url = reverse_lazy('project_app:employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('project_app:employee_list')

class Project_EmployeeCreateView(CreateView, ListView):
    context_object_name = "assignments"
    form_class = Project_EmployeeForm
    model = Project_Employee
    template_name = 'project_app/project_employee_form.html'
    success_url = reverse_lazy('project_app:project_employee_create')    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            print('ERROR FORM INVALID')
            return render(request, self.template_name, {'form': form})

class Project_EmployeeDeleteView(DeleteView):
    model = Project_Employee
    success_url = reverse_lazy('project_app:project_employee_create')

    # def get(self, *args, **kwargs):
    #     return self.delete(*args, **kwargs)
