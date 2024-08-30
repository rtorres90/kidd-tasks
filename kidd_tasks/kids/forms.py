from django import forms
from . import models

class CreateKid(forms.ModelForm):
    class Meta:
        model = models.Kid
        fields = ['first_name', 'last_name', 'nickname', 'dob']