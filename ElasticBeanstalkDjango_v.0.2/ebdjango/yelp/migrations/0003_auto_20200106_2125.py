# Generated by Django 3.0.2 on 2020-01-07 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yelp', '0002_auto_20200106_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraping_test1',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 21, 24, 54, 633783)),
        ),
    ]
