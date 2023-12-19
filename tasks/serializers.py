from rest_framework import serializers
from .models import Task
from datetime import date, datetime

class TaskSerializer(serializers.ModelSerializer):
    """
    A class for a TaskSerializer
    """
#    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
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
            'owner'
            'created_on',
            'title',
            'description',
            'updated_on',
            'priority',
            'category', 
            'state',
            'due_date',
            'assigned_to',
            'profile_id',
            'profile_image',
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
