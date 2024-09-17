from django import forms
from . import models


class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['name', 'description', 'difficulty', 'kid']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'kid': forms.Select(attrs={'class': 'form-select'}),
            'difficulty':forms.Select(attrs={'class': 'form-select'}), 
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        
        self.fields['kid'].queryset = models.Kid.objects.filter(tutor=user)