# Generated by Django 5.0.3 on 2024-03-31 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'Новая'), ('In_progress', 'В работе'), ('Completed', 'Завершена')], default='New', max_length=15)),
                ('priority', models.CharField(choices=[('1', 'Пониженный'), ('2', 'Низкий'), ('3', 'Средний'), ('4', 'Повышенный'), ('5', 'Высокий')], default='3', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bugs', to='tasks.project')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bugs', to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('in_consideration', 'На рассмотрении'), ('accepted', 'Принято'), ('rejected', 'Отклонено')], default='in_consideration', max_length=20)),
                ('priority', models.CharField(choices=[('1', 'Пониженный'), ('2', 'Низкий'), ('3', 'Средний'), ('4', 'Повышенный'), ('5', 'Высокий')], default='3', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_requests', to='tasks.project')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feature_requests', to='tasks.task')),
            ],
        ),
    ]
