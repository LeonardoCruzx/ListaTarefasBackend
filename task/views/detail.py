from task.serializers import TaskSerializer
from task.models import Task
from task.permissions import ReadOnly, IsOwnerOrStaff
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from datetime import datetime

class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsOwnerOrStaff|ReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if(request.data.get("concluded") == "true"):
            request.data["concluded_date"] = datetime.now()
        elif(request.data.get("concluded") == "false"):
            request.data["concluded_date"] = None
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)