from task.serializers import TaskSerializer, TaskSerializerWithCategory
from task.models import Task
from task.permissions import ReadOnly, IsOwnerOrStaff
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import status

class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsOwnerOrStaff|ReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if(request.data.get("concluded", None) is not None):
            concluded = request.data["concluded"]
            request.data["concluded_date"] = datetime.now() if bool(concluded) else None
        task = get_object_or_404(Task,pk=kwargs["pk"])
        request.data["user"] = task.user.id
        task_s = TaskSerializer(task, data=request.data, partial=True)
        if task_s.is_valid():
            task_s.save()
            task_id = task_s.data["id"]
            task = Task.objects.get(pk=task_id)
            task_s = TaskSerializerWithCategory(task)
            return Response(task_s.data)
        return Response({"error":"erro"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)