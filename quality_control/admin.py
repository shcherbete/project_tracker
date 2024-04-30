from django.contrib import admin, messages
from .models import BugReport, FeatureRequest


# Register your models here.


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'description', 'status', 'priority')}),
        ('Links', {'fields': ('project', 'task')})
    )
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('status', 'project', 'task', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    ordering = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

    def set_new_for_selected_bugs(self, request, queryset):
        for bug in queryset:
            bug.status = 'New'
            bug.save()
            messages.success(request, "Success!")

    def set_inProgress_for_selected_bugs(self, request, queryset):
        for bug in queryset:
            bug.status = 'New'
            bug.save()
            messages.success(request, "Success!")

    def set_complete_for_selected_bugs(self, request, queryset):
        for bug in queryset:
            bug.status = 'New'
            bug.save()
            messages.success(request, "Success!")

    actions = [set_new_for_selected_bugs, set_inProgress_for_selected_bugs, set_complete_for_selected_bugs]


# Класс администратора для модели Task
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'description', 'status', 'priority')}),
        ('Links', {'fields': ('project', 'task')})
    )
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('status', 'project', 'task', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    def set_new_for_selected_features(self, request, queryset):
        for feature in queryset:
            feature.status = 'New'
            feature.save()
            messages.success(request, "Success!")

    def set_inProgress_for_selected_features(self, request, queryset):
        for feature in queryset:
            feature.status = 'New'
            feature.save()
            messages.success(request, "Success!")

    def set_complete_for_selected_features(self, request, queryset):
        for feature in queryset:
            feature.status = 'New'
            feature.save()
            messages.success(request, "Success!")

    actions = [set_new_for_selected_features, set_inProgress_for_selected_features, set_complete_for_selected_features]
