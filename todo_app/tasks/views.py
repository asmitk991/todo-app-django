from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo')
    return render(request, 'login.html')

@login_required
def todo(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('todo')


@login_required
def mark_as_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('todo') 


@login_required
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle the status
    task.save()
    return redirect('todo') 
