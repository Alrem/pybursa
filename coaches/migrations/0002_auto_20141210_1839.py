# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dossier', '0001_initial'),
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coaches',
            name='dossier',
            field=models.OneToOneField(to='dossier.Dossier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coaches',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
