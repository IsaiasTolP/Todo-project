from django.shortcuts import redirect
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', lambda _: redirect('tasks:pending-tasks')),
    path('tasks/', views.task_list, name='task-list'),
    path('done/', views.done_tasks, name='done-tasks'),
    path('pending/', views.pending_tasks, name='pending-tasks'),
    path('task/add/', views.add_task, name='add-task'),
    path('task/<task_slug>/toggle/', views.toggle_task, name='toggle-task'),
    path('task/<task_slug>/edit/', views.edit_task, name='edit-task'),
    path('task/<task_slug>/delete/', views.delete_task, name='delete-task'),
]
