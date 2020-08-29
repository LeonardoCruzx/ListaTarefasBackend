from core.views.list import CategoryList

from django.urls import path


urlpatterns = [
    path('list/', CategoryList.as_view(), name="category_list")
]