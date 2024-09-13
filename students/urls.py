from students import views
from django.urls import include, re_path
from django.contrib import admin
from students.views import (
  ListStudentView,
  CreateStudentView,
  UpdateStudentView,
)

app_name = 'students'

urlpatterns = [
    re_path(r'^list-students/$', ListStudentView.as_view(), name='list-students'),
    re_path(r'^create-student/$', CreateStudentView.as_view(), name='create-student'),
    re_path(r'^update-student/(?P<pk>[-\w]+)$', UpdateStudentView.as_view(), name='update-student'),
    re_path(r'^delete-student/(?P<pk>[-\w]+)$', views.delete_student, name='delete-student'),
]