from django.db import models

# Create your models here.
class Coaches(models.Model):

    description = models.CharField(max_length=255)
    SIGNS = (
        ('le', 'lecturer'),
        ('as', 'assistant'),
    )
    sign = models.CharField(max_length=2,
                            choices=SIGNS,
                            default='le')

    course = models.CharField(max_length=255)
