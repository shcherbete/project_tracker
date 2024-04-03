from django.contrib import admin
from .models import BugReport, FeatureRequest

# Register your models here.
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('status', 'project', 'task', 'priority')
    search_fields = ('title', 'description')
    ordering = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'



# Класс администратора для модели Task
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('status', 'project', 'task', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')