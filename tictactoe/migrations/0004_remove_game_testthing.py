# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0003_game_testthing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='testThing',
        ),
    ]
