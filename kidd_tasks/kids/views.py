from django.shortcuts import render, redirect
from . import forms

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