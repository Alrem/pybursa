from django.db import models

# Create your models here.


class Address(models.Model):

    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=40)
    region = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    home = models.CharField(max_length=40)

    def __unicode__(self):
        return self.street + ', ' + self.home