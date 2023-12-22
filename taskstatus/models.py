from django.db import models
from django.contrib.auth.models import User

# Internal:
from states.models import State
from tasks.models import Task

class TaskStatus(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'task']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s task status"
