# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='unloved_courses',
            field=models.ManyToManyField(to='courses.Courses', blank=True),
            preserve_default=True,
        ),
    ]
