from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'done', 'complete_before')
    prepopulated_fields = {'slug': ['name']}
