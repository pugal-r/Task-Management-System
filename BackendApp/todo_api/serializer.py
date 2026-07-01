from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'required': False, 'allow_null': True}
        }