# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Task
from .serializers import TaskSerializer
from anto_prod_app_rest_api.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TaskList(generics.ListCreateAPIView):
    """
    A class to list tasks.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'created_at',
        'due_date',
    ]
    search_fields = [
        'owner__username',
        'title',
        'completed',
        'priority',
    ]
    filterset_fields = [
        'assigned__profile', 
        'completed',
        'priority',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class to display a task detail.
    """
    serializer_class = TaskSerializer

    queryset = Task.objects.all()