from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Coaches(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    ROLES = (
        ('lecturer', 'lecturer'),
        ('assistant', 'assistant'),
    )
    role = models.CharField(max_length=10,
                            choices=ROLES,
                            default='lecturer')
    user = models.ForeignKey(User)
    dossier = models.OneToOneField('dossier.Dossier')


    def __unicode__(self):
        return self.surname + ' ' + self.name
