# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# Internal:
from states.models import State
from categories.models import Category
from priorities.models import Priority
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Task(models.Model):
    """
    A class for the task model
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    is_overdue = models.BooleanField(default=False, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, blank=True,
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    related_name='assigned_to')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        """
        Return information of the Task
        """
        return f"Task: #{self.title}"

