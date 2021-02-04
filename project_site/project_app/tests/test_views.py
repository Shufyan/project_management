from django.http import response
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, reverse_lazy
from project_app.models import Project, Employee, Project_Employee
from project_app.views import ProjectDetailView
from project_app.forms import Project_EmployeeForm
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.project_list_url = reverse('project_app:project_list')
        self.project_create_url = reverse('project_app:project_create')
        self.employee_list_url = reverse('project_app:employee_list')
        self.employee_create_url = reverse('project_app:employee_create')
        self.project_employee_create_url = reverse('project_app:project_employee_create')

    # Project Views
    def test_project_list_view(self):      
        response = self.client.get(self.project_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_app/project_list.html')

    def test_project_detail_view(self): 
        self.project1 = Project.objects.create(
            name = 'TESTPRO00010',
            description = 'API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1',
            start_date = '2021-02-04'
        )
        self.project_detail_url = reverse('project_app:project_detail', args=[self.project1.pk])
        response = self.client.get(self.project_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_app/project_detail.html')

    def test_project_create_view(self): 
        response = self.client.post(self.project_create_url,{
            'name':'TESTPRO00011',
            'description':'API Test 11 API Test 11 API Test 11 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1',
            'start_date':'2021-02-03'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Project.objects.all().count(), 1)

    def test_project_update_view(self):
        self.project1 = Project.objects.create(
            name = 'TESTPRO00012',
            description = 'API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1',
            start_date = '2021-02-04'
        ) 

        self.project_update_url = reverse('project_app:project_update', args=[self.project1.pk])

        response = self.client.post(self.project_update_url,{
            'name':'TESTPRO00013',
            'description':'API Test 11 API Test 11 API Test 11 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1',
            'start_date':'2021-02-03'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Project.objects.all().count(), 1)
        self.assertEqual(Project.objects.get(pk=self.project1.pk).name, 'TESTPRO00013')

    def test_project_delete_view(self):
        self.project1 = Project.objects.create(
            name = 'TESTPRO00014',
            description = 'API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1',
            start_date = '2021-02-04'
        ) 

        self.project_delete_url = reverse('project_app:project_delete', args=[self.project1.pk])

        response = self.client.delete(self.project_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Project.objects.all().count(), 0)

    # Employee Views
    def test_employee_list_view(self):      
        response = self.client.get(self.employee_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_app/employee_list.html')

    def test_employee_detail_view(self): 
        self.employee1 = Employee.objects.create(
            fullname = 'First Employee'            
        )
        self.employee_detail_url = reverse('project_app:employee_detail', args=[self.employee1.pk])
        response = self.client.get(self.employee_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_app/employee_detail.html')

    def test_employee_create_view(self): 
        response = self.client.post(self.employee_create_url,{
            'fullname':'Second Employee'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.all().count(), 1)

    def test_employee_update_view(self):
        self.employee1 = Employee.objects.create(
            fullname = 'Third Employee'
        ) 

        self.employee_update_url = reverse('project_app:employee_update', args=[self.employee1.pk])

        response = self.client.post(self.employee_update_url,{
            'fullname':'Fourth Employee'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.all().count(), 1)
        self.assertEqual(Employee.objects.get(pk=self.employee1.pk).fullname, 'Fourth Employee')

    def test_employee_delete_view(self):
        self.employee1 = Employee.objects.create(
            fullname = 'Fifth Employee'
        ) 

        self.employee_delete_url = reverse('project_app:employee_delete', args=[self.employee1.pk])

        response = self.client.delete(self.employee_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.all().count(), 0)

    # Assignment Views
    def test_project_employee_create_view(self): 
        form = Project_EmployeeForm()
        self.project1 = Project.objects.create(
            name = 'TESTPROEMP001',
            description = 'This project is created to test assignment functionality.',
            start_date = '2021-02-04'
        )
        self.employee1 = Employee.objects.create(
            fullname = 'Assignment Employee'
        )
        response = self.client.post(self.project_employee_create_url,{
            'project': self.project1,
            'employee': self.employee1 
        })
        Project_Employee.objects.create(
            project = self.project1,
            employee = self.employee1
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Project_Employee.objects.all().count(), 1)
        self.assertTrue(Project_Employee.objects.filter(project=self.project1.id).exists())
        self.assertFalse(form.is_valid())

    def test_project_employee_delete_view(self):
        self.project1 = Project.objects.create(
            name = 'TESTPROEMP002',
            description = 'This project is created to test assignment functionality.',
            start_date = '2021-02-04'
        )
        self.employee1 = Employee.objects.create(
            fullname = 'Assignment Two Employee'
        ) 

        self.proemp1 = Project_Employee.objects.create(
            project = self.project1,
            employee = self.employee1
        )

        self.project_employee_delete_url = reverse('project_app:project_employee_delete', args=[self.proemp1.pk])

        response = self.client.delete(self.project_employee_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Project_Employee.objects.all().count(), 0)
