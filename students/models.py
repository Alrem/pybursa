from django.db import models

# Create your models here.

from courses.models import Courses
from dossier.models import Dossier
from django import forms
from django.utils.translation import ugettext_lazy as _

class Student(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    courses = models.ManyToManyField(Courses)
    package = models.CharField(max_length=15)
    dossier = models.OneToOneField(Dossier)

    def __unicode__(self):
        return self.surname + ' ' + self.name


class StudentForm(forms.Form):
    student_name = forms.CharField(max_length=100)
    student_surname = forms.CharField(max_length=255)
    student_email = forms.EmailField()
    student_phone = forms.CharField(max_length=15)
    student_package = forms.CharField(max_length=15)