from django.contrib import admin
from .models import Project, Employee, Project_Employee

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'start_date']
    list_display = ('id', 'name', 'start_date')

class EmployeeAdmin(admin.ModelAdmin):
    fields = ['fullname']
    list_display = ('id', 'fullname')

class Project_EmployeeAdmin(admin.ModelAdmin):
    fields = ['project_id', 'employee_id']
    list_display = ('id', 'project_id', 'employee_id')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project_Employee, Project_EmployeeAdmin)
