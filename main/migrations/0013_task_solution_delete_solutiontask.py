# Generated by Django 4.0.5 on 2022-08-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_task_solution_solutiontask'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='solution',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='SolutionTask',
        ),
    ]