from user.views.auth import UserAuth

from django.urls import path

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/', UserAuth.as_view(), name='user_auth'),
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]