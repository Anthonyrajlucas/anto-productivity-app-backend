from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Priority

class PriorityList(APIView):

    def get(self, request):
        priorities = Priority.objects.all()
        serializer = PrioritySerializer(priorities, many= True)
        return Response(serializer.data)