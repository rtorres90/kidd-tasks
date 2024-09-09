from django.shortcuts import render, redirect
from . import forms
from .models import Kid
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_view(request):
    if request.method == "POST":
        form = forms.CreateKid(request.POST)
        if form.is_valid():
            new_kid = form.save(commit=False)
            new_kid.tutor = request.user
            new_kid.save()
            return redirect("/")
    else:
        form = forms.CreateKid()
    return render(request, 'kids/create.html', {'form': form})

@login_required(login_url='/users/login')
def list_view(request):
    if request.user:
        kids = Kid.objects.all().filter(tutor=request.user)
    return render(request, 'kids/list.html', {'kids': kids})