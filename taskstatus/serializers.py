from rest_framework import serializers
from .models import TaskStatus
from datetime import date, datetime

class TaskStatusSerializer(serializers.ModelSerializer):
    """
    A class for a TaskStatusSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            'id',
            'is_owner',
            'owner',
            'created_on',
            'updated_on',
            'state',
            'profile_id'
        ]
        read_only_fields = ['owner']
     
