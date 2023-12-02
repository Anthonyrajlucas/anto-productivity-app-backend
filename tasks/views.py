from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework import status

class TaskList(APIView):

    def get(self, request):
        title_query = request.GET.get('title', '')
        priority_query = request.GET.get('priority', '')
        category_query = request.GET.get('category', '')
        state_query = request.GET.get('state', '')
        
        if title_query:
            tasks = Task.objects.filter(Q(title__icontains=title_query))
        elif priority_query:
            tasks = Task.objects.filter(Q(priority__name__icontains=priority_query))
        elif category_query:
            tasks = Task.objects.filter(Q(category__name__icontains=category_query))
        elif state_query:
            tasks = Task.objects.filter(Q(state__name__icontains=state_query))        
        else:
            tasks = Task.objects.all()
            
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

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