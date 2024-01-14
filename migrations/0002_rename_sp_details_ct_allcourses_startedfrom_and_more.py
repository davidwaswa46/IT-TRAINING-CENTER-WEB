# Generated by Django 5.0.1 on 2024-01-09 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechGuru', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='sp',
            new_name='ct',
        ),
        migrations.AddField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateField(default=datetime.datetime(2024, 1, 9, 4, 57, 33, 696507, tzinfo=datetime.timezone.utc), verbose_name='Started from'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='your_choice',
            field=models.BooleanField(default=False),
        ),
    ]
