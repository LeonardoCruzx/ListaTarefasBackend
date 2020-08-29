from user.views.auth import UserAuth
from user.views.list import UserList
from user.views.detail import UserDetail

from django.urls import path

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/', UserAuth.as_view(), name='user_auth'),
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserList.as_view(), name="user_list"),
    path('detail/<int:pk>/', UserDetail.as_view(), name="user_detail")
]