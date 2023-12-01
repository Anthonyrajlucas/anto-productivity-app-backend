from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User 


class TaskSerializer(serializers.ModelSerializer):
    assigned = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    priority = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    state = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 'is_overdue', 'file_attachment',
            'assigned', 'priority', 'category', 'state', 'created_at', 'updated_at'
        ]


