from task.models import Task
from task.serializers import TaskSerializer
from task.paginators import TaskPaginator
from task.permissions import IsOwnerOrStaff, ReadOnly


from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework import filters
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie



class TaskList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPaginator
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['category','user']
    ordering_fields = ['created_at','final_date']

    @method_decorator(cache_page(5))
    @method_decorator(vary_on_cookie)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return super().post(request, *args, **kwargs)