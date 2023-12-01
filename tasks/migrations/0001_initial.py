# Generated by Django 4.2.7 on 2023-12-01 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('priorities', '0001_initial'),
        ('states', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField()),
                ('is_overdue', models.BooleanField(default=False)),
                ('file_attachment', models.FileField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned', models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priorities.priority')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.state')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
