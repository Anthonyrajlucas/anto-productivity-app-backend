# Generated by Django 4.2.7 on 2023-12-19 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_options_rename_created_at_task_created_on_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
    ]