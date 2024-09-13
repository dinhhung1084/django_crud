from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    from_city = models.CharField(max_length=100, null=False, blank=False) 

    def __unicode__(self):
       return self.content
    def get_absolute_url(self):
       return reverse('students:list-students', kwargs={})