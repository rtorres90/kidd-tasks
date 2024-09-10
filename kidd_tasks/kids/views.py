from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Kid
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login')
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

@login_required(login_url='/users/login')
def edit_view(request, kid_id):
    kid = get_object_or_404(Kid, id=kid_id)
    if request.method == 'POST':
        form = forms.CreateKid(request.POST, instance=kid)
        if form.is_valid():
            form.save()
            return redirect("kids:list")
    else:
        form = forms.CreateKid(instance=kid)
    return render(request, "kids/edit.html", {'form': form})