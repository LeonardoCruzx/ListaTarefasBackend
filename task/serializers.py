from task.models import Task
from core.serializers import CategorySerializer

from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        
class TaskSerializerWithCategory(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Task
        fields = "__all__"