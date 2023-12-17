from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, Priority, Category
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework import status

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    filterset_fields = [
        'assigned__profile',  
    ]

    search_fields = [
        'title',
        'priority__name',
        'category__name',
        'state__name',
    ]

    ordering_fields = [
        'created_at',
        'due_date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

