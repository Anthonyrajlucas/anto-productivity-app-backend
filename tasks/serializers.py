from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned = serializers.StringRelatedField(many=True)
    priority = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    state = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 'is_overdue', 'file_attachment',
            'assigned', 'priority', 'category', 'state', 'created_at', 'updated_at'
        ]


