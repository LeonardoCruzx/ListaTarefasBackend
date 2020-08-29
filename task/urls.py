from task.views.list import TaskList

from django.urls import path



urlpatterns = [
    path('list/', TaskList.as_view(), name="task_list")
]