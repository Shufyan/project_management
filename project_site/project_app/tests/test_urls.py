from django.test import SimpleTestCase
from django.urls import resolve, reverse
from project_app.views import (ProjectListView, ProjectDetailView, ProjectCreateView,
                                ProjectUpdateView, ProjectDeleteView, EmployeeListView,
                                EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,
                                EmployeeDetailView, Project_EmployeeCreateView, Project_EmployeeDeleteView)

class TestUrLs(SimpleTestCase):

    # Project URLs
    def test_project_list_url_is_resolved(self):
        url = reverse('project_app:project_list')
        self.assertEquals(resolve(url).func.view_class, ProjectListView)

    def test_project_detail_url_is_resolved(self):
        url = reverse('project_app:project_detail', args=[111])
        self.assertEquals(resolve(url).func.view_class, ProjectDetailView)

    def test_project_create_url_is_resolved(self):
        url = reverse('project_app:project_create')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_project_update_url_is_resolved(self):
        url = reverse('project_app:project_update', args=[111])
        self.assertEquals(resolve(url).func.view_class, ProjectUpdateView)

    def test_project_delete_url_is_resolved(self):
        url = reverse('project_app:project_delete', args=[111])
        self.assertEquals(resolve(url).func.view_class, ProjectDeleteView)

    # Employee Urls
    def test_employee_list_url_is_resolved(self):
        url = reverse('project_app:employee_list')
        self.assertEquals(resolve(url).func.view_class, EmployeeListView)

    def test_employee_detail_url_is_resolved(self):
        url = reverse('project_app:employee_detail', args=['BgeoWh'])
        self.assertEquals(resolve(url).func.view_class, EmployeeDetailView)

    def test_employee_create_url_is_resolved(self):
        url = reverse('project_app:employee_create')
        self.assertEquals(resolve(url).func.view_class, EmployeeCreateView)

    def test_employee_update_url_is_resolved(self):
        url = reverse('project_app:employee_update', args=['BgeoWh'])
        self.assertEquals(resolve(url).func.view_class, EmployeeUpdateView)

    def test_employee_delete_url_is_resolved(self):
        url = reverse('project_app:employee_delete', args=['BgeoWh'])
        self.assertEquals(resolve(url).func.view_class, EmployeeDeleteView)

    # Assignment URLs
    def test_project_employee_create_url_is_resolved(self):
        url = reverse('project_app:project_employee_create')
        self.assertEquals(resolve(url).func.view_class, Project_EmployeeCreateView)

    def test_project_employee_delete_url_is_resolved(self):
        url = reverse('project_app:project_employee_delete', args=[100])
        self.assertEquals(resolve(url).func.view_class, Project_EmployeeDeleteView)