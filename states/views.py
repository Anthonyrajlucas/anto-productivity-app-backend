from rest_framework.views import APIView
from rest_framework.response import Response
from .models import State
from .serializers import StateSerializer
from django.http import Http404
from rest_framework import status

class StateList(APIView):

    def get(self, request):
        states = State.objects.all()
        serializer = StateSerializer(states, many= True)
        return Response(serializer.data)

class StateDetail(APIView):
    serializer_class = StateSerializer
    def get_object(self, pk):
        try:
            state=State.objects.get(pk=pk)
            return state
        except State.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        state = self.get_object(pk)
        serializer=StateSerializer(state)
        return Response(serializer.data)

    def put (self, request, pk):
        state =self.get_object(pk)
        serializer=StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



