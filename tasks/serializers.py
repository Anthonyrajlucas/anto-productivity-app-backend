from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from datetime import date, datetime

class TaskSerializer(serializers.ModelSerializer):
    assigned = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 'file_attachment',
            'assigned', 'priority', 'category', 'state', 'created_at', 'updated_at', 'owner'
        ]
        read_only_fields = ['is_overdue']

    def to_representation(self, instance):
        representation = super(TaskSerializer, self).to_representation(instance)
        today = date.today()
        due_date_str = representation.get('due_date')

        if due_date_str:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            representation['is_overdue'] = due_date < today
        else:
            representation['is_overdue'] = False

        return representation
