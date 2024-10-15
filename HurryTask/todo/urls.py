from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),  # todo:home
    path('tasks/<task_slug>/', views.task_detail, name='task_detail'),  # todo:task_detail
    path('task/create/', views.create_task, name='create-task'), #todo:create-task
]
