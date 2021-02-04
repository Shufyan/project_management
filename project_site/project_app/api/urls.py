from django.urls import include, path
from django.conf.urls import url
from . import views
from rest_framework import routers
# from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
# schema_view = get_swagger_view(title='Product Management API')

schema_view = get_schema_view(
   openapi.Info(
      title="Project Management API",
      default_version='v1',
      description="A list of API's schema for Project Management application.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@projectmgmt.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = "api"

urlpatterns = [
    url(r'drf/', include(router.urls)),
    # url(r'swagger/', schema_view),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

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