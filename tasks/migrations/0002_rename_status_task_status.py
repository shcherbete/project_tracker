# Generated by Django 5.0.3 on 2024-04-03 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='STATUS',
            new_name='status',
        ),
    ]