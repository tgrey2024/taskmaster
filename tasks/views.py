from django.shortcuts import render, redirect
from .models import Task, Category
from .forms import TaskForm

def home(request):
    to_do_tasks = Task.objects.filter(completed=False)
    done_tasks = Task.objects.filter(completed=True)
    form = TaskForm()
    return render(request, 'tasks/index.html', {'to_do_tasks': to_do_tasks, 'done_tasks': done_tasks, 'form': form})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})