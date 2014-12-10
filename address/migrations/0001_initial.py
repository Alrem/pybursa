# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=40)),
                ('region', models.CharField(max_length=40)),
                ('district', models.CharField(max_length=40)),
                ('street', models.CharField(max_length=40)),
                ('home', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
