from django import forms
from .models import Project, Employee, Project_Employee
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput 

class ProjectForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-md'}), label='')
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'md-textarea form-control form-control-md','rows':5}), label='')

    class Meta:
        model = Project
        fields = '__all__'

        widgets = {            
            'start_date': DatePickerInput(attrs={'style':'margin-left:40px; max-width:400px;','class':'form-control form-control-md'},
                options={
                        "format": "YYYY-MM-DD", # moment date-time format
                        }
                ), # default date-format %m/%d/%Y will be used             
            }

class EmployeeForm(forms.ModelForm):

    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-md'}), label='')

    class Meta:
        model = Employee
        fields = '__all__'



class Project_EmployeeForm(forms.ModelForm): 

    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="- Select Project -", widget=forms.Select(attrs={'class':'w3-select', 'style':'margin-right:20px; max-width:200px;'}), label='')    
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="- Select Employee -", widget=forms.Select(attrs={'class':'w3-select', 'style':'margin-right:20px; max-width:200px;'}), label='')    

    class Meta:
        model = Project_Employee
        fields = '__all__'

        
    