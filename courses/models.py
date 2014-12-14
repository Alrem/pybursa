from django.db import models

# Create your models here.

from coaches.models import Coaches
from address.models import Address

class Courses(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    instructor = models.ForeignKey(Coaches)
    assistant = models.ForeignKey(Coaches, related_name='+')
    start_date = models.DateField()
    end_date = models.DateField()
    technology = models.CharField(max_length=255)
    venue = models.ForeignKey(Address)
    slug = models.SlugField()


    def __unicode__(self):
        return self.title