from django.db import models

# Create your models here.
from address.models import Address


class Dossier(models.Model):

    address = models.ForeignKey(Address)
    unloved_courses = models.ManyToManyField('courses.Courses', blank=True)
    COLORS = (
        ('red', 'red'),
        ('orange', 'orange'),
        ('yellow', 'yellow'),
        ('green', 'green'),
        ('cyan', 'cyan'),
        ('blue', 'blue'),
        ('purple', 'purple'),
    )
    color = models.CharField(max_length=6,
                            choices=COLORS,
                            default='purple')

    def __unicode__(self):
        return self.color
