from task.views.list import TaskList
from task.views.detail import TaskDetail

from django.urls import path



urlpatterns = [
    path('list/', TaskList.as_view(), name="task_list"),
    path('detail/<int:pk>/', TaskDetail.as_view(), name="task_detail")
]