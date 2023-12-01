from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Priority
from .serializers import PrioritySerializer
from django.http import Http404
from rest_framework import status

class PriorityList(APIView):

    def get(self, request):
        priorities = Priority.objects.all()
        serializer = PrioritySerializer(priorities, many= True)
        return Response(serializer.data)

class PriorityDetail(APIView):
    serializer_class = PrioritySerializer
    def get_object(self, pk):
        try:
            priority=Priority.objects.get(pk=pk)
            return priority
        except Priority.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        priority = self.get_object(pk)
        serializer=PrioritySerializer(priority)
        return Response(serializer.data)

    def put (self, request, pk):
        priority =self.get_object(pk)
        serializer=PrioritySerializer(priority, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

