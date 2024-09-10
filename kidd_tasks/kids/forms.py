from django import forms
from . import models

class CreateKid(forms.ModelForm):
    class Meta:
        model = models.Kid
        fields = ['first_name', 'last_name', 'nickname', 'dob']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime'}),
        }
