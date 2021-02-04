from django.test import TestCase
from project_app.models import Project, Employee, Project_Employee

class TestModels(TestCase):
    
    def setUp(self):
        self.project1 = Project.objects.create(
            name = 'TESTPRO0001',
            description = 'This project is created to testing. This project is created to testing. This project is created to testing. This project is created to testing.',
            start_date = '2021-02-04'
        )
        self.employee1 = Employee.objects.create(
            fullname = 'First Test Employee'            
        )
        self.proemp1 = Project_Employee.objects.create(
            project = self.project1,
            employee = self.employee1
        )
 
    def test_project_model_created(self):
        self.assertTrue(Project.objects.filter(id=self.project1.id).exists())

    def test_employee_model_created(self):
        self.assertTrue(Employee.objects.filter(id=self.employee1.id).exists())

    def test_project_employee_model_created(self):
        self.assertTrue(Project_Employee.objects.filter(id=self.proemp1.id).exists())