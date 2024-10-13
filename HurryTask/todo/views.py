from django.shortcuts import render

from todo.models import Task


def home(request):
    tasks = Task.objects.all()
    num_tasks = Task.objects.count()
    done_tasks, not_done_tasks = [], []
    [done_tasks.append(task) if task.done else not_done_tasks.append(task) for task in tasks]
    return render(request, 
                'todo/home.html', 
                {'tasks': tasks, 'num_tasks': num_tasks, 'done_tasks': done_tasks, 'not_done_tasks': not_done_tasks})


def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'todo/tasks/detail.html', {'task': task})
