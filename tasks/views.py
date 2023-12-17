from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework import status

class TaskList(generics.ListAPIView):
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

class TaskDetail(APIView):
    serializer_class = TaskSerializer

    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        priority = get_object_or_404(Priority, pk=request.data.get('priority'))
        category = get_object_or_404(Category, pk=request.data.get('category'))

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

