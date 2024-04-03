from django.db import models

from tasks.models import Project, Task


# Create your models here.
class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена')
    ]
    PRIORITY_CHOICES = [
        ('1', 'Пониженный'),
        ('2', 'Низкий'),
        ('3', 'Средний'),
        ('4', 'Повышенный'),
        ('5','Высокий')
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bugs',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bugs',
        on_delete=models.SET_NULL,
        null=True,
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='New')
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='3')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('in_consideration', 'На рассмотрении'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено')
    ]
    PRIORITY_CHOICES = [
        ('1', 'Пониженный'),
        ('2', 'Низкий'),
        ('3', 'Средний'),
        ('4', 'Повышенный'),
        ('5', 'Высокий')
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='feature_requests',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_consideration')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='3')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
