from django.db import models

# Create your models here.
from django import forms
from coaches.models import Coaches
from students.models import Student

class Contacts(models.Model):

    subject = models.CharField(max_length=255)
    recipient = models.ForeignKey(Coaches)
    victim = models.ForeignKey(Student)
    message = models.TextField()
