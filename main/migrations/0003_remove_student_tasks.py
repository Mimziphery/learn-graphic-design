# Generated by Django 4.0.5 on 2022-08-26 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_solutions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='tasks',
        ),
    ]
