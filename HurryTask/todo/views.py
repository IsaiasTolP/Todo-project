from django.shortcuts import redirect, render
from django.utils.text import slugify
from todo.models import Task
from .forms import CreateTaskForm


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


def create_task(request):
    if request.method == 'POST':
        if (form := CreateTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('todo:home')
    else:
        form = CreateTaskForm()
    return render(request, 'todo/task/create_task.html', dict(form=form))