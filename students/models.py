from django.db import models

# Create your models here.

from courses.models import Courses
from dossier.models import Dossier

class Student(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    courses = models.ManyToManyField(Courses)
    package = models.CharField(max_length=15)
    dossier = models.OneToOneField(Dossier)
