# Generated by Django 3.1.3 on 2020-11-22 02:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201121_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 2, 8, 42, 451602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 2, 8, 42, 450954, tzinfo=utc)),
        ),
    ]
