# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('technology', models.CharField(max_length=255)),
                ('assistant', models.ForeignKey(related_name='+', to='coaches.Coaches')),
                ('instructor', models.ForeignKey(to='coaches.Coaches')),
                ('venue', models.ForeignKey(to='address.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
