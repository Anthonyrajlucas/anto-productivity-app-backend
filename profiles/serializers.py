from rest_framework import serializers

# Internal:
from .models import Profile
from tasks.models import Task
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProfileSerializer(serializers.ModelSerializer):
    """
    A class for a ProfileSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    tasks_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'created_on',
            'updated_on',
            'image',
            'is_owner',
            'tasks_count',
        ]