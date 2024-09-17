from django.shortcuts import render, redirect
from .forms import CreateTask
from kids.models import Kid
from .models import Task

def create_view(request):
    if request.method == "POST":
        form = CreateTask(request.POST, user=request.user)
        if form.is_valid():
            form.save()
        return redirect("tasks:list")
    else:
        form = CreateTask(user=request.user)
    return render(request, "tasks/create.html", {'form': form})

def list_view(request):
    if request.method == "GET":
        kids = Kid.objects.all().filter(tutor=request.user)
        tasks = Task.objects.filter(kid__in=kids)
        return render(request, "tasks/list.html", {'tasks': tasks}) 
