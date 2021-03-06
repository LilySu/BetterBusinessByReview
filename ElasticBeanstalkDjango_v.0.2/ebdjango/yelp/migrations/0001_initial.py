# Generated by Django 3.0.2 on 2020-01-07 02:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='business_id_test1',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('biz_id', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='scraping_test1',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('review_id', models.CharField(blank=True, max_length=5000)),
                ('business_id', models.CharField(blank=True, max_length=30)),
                ('stars', models.FloatField(blank=True, max_length=10, null=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2020, 1, 6, 21, 22, 21, 269956))),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(auto_now_add=True)),
                ('text', models.CharField(blank=True, max_length=100000)),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
