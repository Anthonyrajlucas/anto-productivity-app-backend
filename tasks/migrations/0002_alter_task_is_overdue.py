# Generated by Django 4.2.7 on 2023-12-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_overdue',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
