from django.shortcuts import render
from .forms import CreateTask

def create_view(request):
    if request.method == "POST":
        pass
    else:
        form = CreateTask()
    
    return render(request, "tasks/create.html", {'form': form})
