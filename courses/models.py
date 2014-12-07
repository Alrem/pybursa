from django.db import models

# Create your models here.

class Courses(models.Model):

    language = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    assistant = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

