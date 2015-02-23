# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misDatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='misdatos',
            name='facebook',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='misdatos',
            name='imagen',
            field=models.FileField(default=' ', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='misdatos',
            name='twitter',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='misdatos',
            name='youtube',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]
