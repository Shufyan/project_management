from django.urls import path
from django.conf.urls import url

from . import views

app_name = "project_app"

urlpatterns = [    
    url(r'^projects/create/',views.ProjectCreateView.as_view() ,name='project_create'),
    url(r'^projects/(?P<pk>\d+)/update/$', views.ProjectUpdateView.as_view(), name="project_update"),
    url(r'^projects/(?P<pk>\d+)/delete/$', views.ProjectDeleteView.as_view(), name='project_delete'),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name="project_detail"),   
    url(r'^projects/', views.ProjectListView.as_view(), name="project_list"),
    url(r'^employees/create/',views.EmployeeCreateView.as_view() ,name='employee_create'),
    url(r'^employees/(?P<pk>[-\w]+)/update/$', views.EmployeeUpdateView.as_view(), name="employee_update"),
    url(r'^employees/(?P<pk>[-\w]+)/delete/$', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    url(r'^employees/(?P<pk>[-\w]+)/$', views.EmployeeDetailView.as_view(), name="employee_detail"),   
    url(r'^employees/', views.EmployeeListView.as_view(), name="employee_list"), 
]