from django.shortcuts import redirect, render
from django.utils.text import slugify

from tasks.models import Task

from .forms import AddTaskForm, EditTaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(
        request,
        'tasks/taskList.html',
        {
            'tasks': tasks,
            'title': 'Your tasks',
            'no_tasks_msg': 'You do not have any task created',
        },
    )


def done_tasks(request):
    tasks = Task.objects.filter(done=True)
    return render(
        request,
        'tasks/taskList.html',
        {
            'tasks': tasks,
            'title': 'Done tasks',
            'no_tasks_msg': 'You have not done any task :(',
        },
    )


def pending_tasks(request):
    tasks = Task.objects.filter(done=False)
    return render(
        request,
        'tasks/taskList.html',
        {
            'tasks': tasks,
            'title': 'Pending tasks',
            'no_tasks_msg': 'You do not have any task pending',
        },
    )


def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(
        request,
        'tasks/detail.html',
        {
            'task': task,
        },
    )


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = AddTaskForm()
    return render(request, 'tasks/task-form.html', dict(form=form))


def toggle_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.done = not task.done
    task.save()
    return redirect('tasks:task-list')


def edit_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = EditTaskForm(instance=task)
    return render(request, 'tasks/task-form.html', dict(form=form))


def delete_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.delete()
    return redirect('tasks:task-list')
