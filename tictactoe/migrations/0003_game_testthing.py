# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0002_game_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='testThing',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Test one'), (b'B', b'Test two')]),
        ),
    ]
