from django.db import models
from django.contrib.auth.models import User
from states.models import State
from categories.models import Category
from priorities.models import Priority

class Task(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    is_overdue = models.BooleanField(default=False, editable=False)
    file_attachment = models.FileField(upload_to='images/', null=True, blank=True)
    assigned = models.ManyToManyField(User, related_name='tasks')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']
