# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import TaskStatus
from .serializers import TaskStatusSerializer
from anto_prod_app_rest_api.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TaskStatusList(generics.ListCreateAPIView):
    """
    A class to list tasks.
    """
    serializer_class = TaskStatusSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = TaskStatus.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class to display a task detail.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()

