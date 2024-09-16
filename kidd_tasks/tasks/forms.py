from django import forms
from . import models

class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['name', 'description', 'difficulty']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'difficulty': forms.RadioSelect(attrs={'class': 'form-control'}),
        }
