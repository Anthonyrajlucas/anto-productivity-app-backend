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
   

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TaskStatus
        fields = [
            'id',
            'is_owner',
            'owner',
           'created_at', 
           'updated_at',
            'state',
            'task',
            'profile_id'
        ]
        read_only_fields = ['owner']
     
def update(self, instance, validated_data):
        instance.created_on = timezone.now()
        return super().update(instance, validated_data)