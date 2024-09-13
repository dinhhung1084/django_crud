from django import forms
from .models import Student

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone', 'email', 'age', 'from_city']