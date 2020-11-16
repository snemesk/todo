from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def home(request):
    all_items = Task.objects.all
    return render(request, 'index.html', {'all_items': all_items})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'create_tasks.html', {'form': form})

def edit_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit.html', {'form': form}, {'task':task})

def delete(request, task_id):
    item = Task.objects.get(id=task_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted from List!'))
    return redirect('home')