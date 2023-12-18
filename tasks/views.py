from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, Priority, Category
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework import status
from anto_prod_app_rest_api.permissions import IsOwnerOrReadOnly

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
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
        owner = self.request.user if self.request.user.is_authenticated else None
        serializer.save(owner=owner)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        self.check_object_permissions(self.request, task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
       
