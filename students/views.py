
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CreateStudentForm
from .models import Student

class ListStudentView(ListView):
  model = Student
  def get(self, request, *args, **kwargs):
    template_name = 'students/list-students.html'
    obj = {
      'students': Student.objects.all()
    }
    return render(request, template_name, obj)

class CreateStudentView(SuccessMessageMixin, CreateView):
  template_name = 'students/create-student.html'
  form_class = CreateStudentForm
  success_message = 'Create Student successfully!'
  
  
class UpdateStudentView(SuccessMessageMixin, UpdateView):
  template_name = 'students/edit-student.html'
  model = Student
  fields =  ['name', 'phone', 'email', 'age', 'from_city']
  success_message = 'Update Student successfully!'
  def get_success_url(self): 
    return reverse('students:list-students', kwargs={})


def delete_student(request, pk):
    Student = Student.objects.filter(id=pk)
    Student.delete()
    context = {
      "messages": "Delete Student successfully",
      'students': Student.objects.all()
    }              
    return render(request, 'students/list-students.html', context)

