from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateTask
from kids.models import Kid
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login')
def create_view(request):
    if request.method == "POST":
        form = CreateTask(request.POST, user=request.user)
        if form.is_valid():
            form.save()
        return redirect("tasks:list")
    else:
        form = CreateTask(user=request.user)
    return render(request, "tasks/create.html", {'form': form})

@login_required(login_url='/users/login')
def list_view(request):
    if request.method == "POST":
        selected_kid = request.POST.get('kid')
    else:
        selected_kid = 'All'

    kids = Kid.objects.all().filter(tutor=request.user)

    if selected_kid and selected_kid != 'All':
        selected_kid = int(selected_kid) 
        tasks = Task.objects.filter(kid__id=selected_kid)
    else:
        tasks = Task.objects.filter(kid__in=kids)
    
    return render(request, "tasks/list.html", {'tasks': tasks, 'kids':kids, 'selected_kid':selected_kid})

@login_required(login_url='/users/login')
def edit_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("tasks:list")
    else:
        form = CreateTask(instance=task, user=request.user)
    return render(request, "tasks/edit.html", {'form': form, 'task':task})