from django.db.models import Count
from rest_framework import status, generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer
from anto_prod_app_rest_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    """
    A class to list all profiles
    No Create view (post method), as profile creation
    handled by django signals
    """
    serializer_class = ProfileSerializer
    profiles = Profile.objects.all()   

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for a profile detail.
    """
    serializer_class = ProfileSerializer
#    permission_classes = [IsOwnerOrReadOnly]
    profiles = Profile.objects.all()
class UserList(APIView):
    """
    A class to list all site users.
    """
    def get(self, request):
        users = User.objects.all().values()
        return Response(users)
