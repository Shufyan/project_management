from django.test import TestCase
from project_app.forms import ProjectForm, EmployeeForm, Project_EmployeeForm
from project_app.models import Project, Employee

class TestForms(TestCase):      

    def setUp(self):
        self.project1 = Project.objects.create(
            name = 'TESTPRO0001',
            description = 'This project is created to testing. This project is created to testing. This project is created to testing. This project is created to testing.',
            start_date = '2021-02-04'
        )
        self.employee1 = Employee.objects.create(
            fullname = 'First Test Employee'            
        )  

    def test_project_form_valid_data(self):
        form = ProjectForm(data={
            'name':'TESTPRO00013',
            'description':'API Test 11 API Test 11 API Test 11 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1 API Test 1',
            'start_date':'2021-02-03'
        })

        self.assertTrue(form.is_valid())

    def test_project_form_no_data(self):
        form = ProjectForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_employee_form_valid_data(self):
        form = EmployeeForm(data={
            'fullname':'Test Employee'
        })

        self.assertTrue(form.is_valid())

    def test_employee_form_no_data(self):
        form = EmployeeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_project_employee_form_valid_data(self):        

        form = Project_EmployeeForm(data={
            'project': self.project1,
            'employee': self.employee1
        })

        self.assertTrue(form.is_valid())