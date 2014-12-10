# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(default=b'purple', max_length=6, choices=[(b'red', b'red'), (b'orange', b'orange'), (b'yellow', b'yellow'), (b'green', b'green'), (b'cyan', b'cyan'), (b'blue', b'blue'), (b'purple', b'purple')])),
                ('address', models.ForeignKey(to='address.Address')),
                ('unloved_courses', models.ManyToManyField(to='courses.Courses')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
