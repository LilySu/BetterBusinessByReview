# Generated by Django 3.0 on 2019-12-16 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WordListAPI',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('word_phrase', models.CharField(max_length=50)),
                ('high_rating_score', models.DecimalField(decimal_places=2, max_digits=3)),
                ('low_rating_score', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=5000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('word_phrase', models.CharField(max_length=50)),
                ('high_rating_score', models.DecimalField(decimal_places=2, max_digits=3)),
                ('low_rating_score', models.DecimalField(decimal_places=2, max_digits=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]