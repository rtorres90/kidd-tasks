from django.db import models

from kidd_tasks.kids.models import Kid


class Tag(models.Model):
    name = models.CharField(max_length=20)

class Task(models.Model):
    name = models.CharField(max_length=20)
    difficulty = models.IntegerField(
        choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)],
        default=1,
        help_text="Difficulty of the task, from 1 to 5 starts."
    )
    description = models.TextField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name='tasks') 
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)