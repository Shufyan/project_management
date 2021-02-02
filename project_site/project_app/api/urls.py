from django.urls import include, path
from django.conf.urls import url
from . import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
schema_view = get_swagger_view(title='Product Management API')

app_name = "api"

urlpatterns = [
    url(r'drf/', include(router.urls)),
    url(r'swagger/', schema_view),

    url(r'projects/create/',views.ApiProjectCreateView.as_view()),
    url(r'projects/(?P<pk>\d+)/$', views.ApiProjectDetailView.as_view()),
    url(r'projects/(?P<pk>\d+)/update/$', views.ApiProjectUpdateView.as_view()),
    url(r'projects/(?P<pk>\d+)/delete/$', views.ApiProjectDeleteView.as_view()),
    url(r'projects/', views.ApiProjectListView.as_view()),    

    url(r'employees/create/',views.ApiEmployeeCreateView.as_view()),
    url(r'employees/(?P<pk>[-\w]+)/update/$', views.ApiEmployeeUpdateView.as_view()),
    url(r'employees/(?P<pk>[-\w]+)/delete/$', views.ApiEmployeeDeleteView.as_view()),
    url(r'employees/(?P<pk>[-\w]+)/$', views.ApiEmployeeDetailView.as_view()),   
    url(r'employees/', views.ApiEmployeeListView.as_view()),

    url(r'^project_employee/create/',views.ApiProject_EmployeeCreateView.as_view()),
    url(r'^project_employee/(?P<pk>\d+)/delete/$', views.ApiProject_EmployeeDeleteView.as_view()),
]