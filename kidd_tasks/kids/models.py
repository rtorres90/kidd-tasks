from django.db import models
from django.contrib.auth.models import User

class Kid(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    dob = models.DateTimeField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
