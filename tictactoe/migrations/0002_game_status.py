# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Active'), (b'F', b'First Player Wins'), (b'S', b'Second Player Wins'), (b'D', b'Draw')]),
        ),
    ]
