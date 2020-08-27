from user.models import User
from user.serializers import UserSerializer

from django.db import IntegrityError
from django.core.exceptions import ValidationError

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

class UserAuth(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if(User.check_credentials(request)):
            user = authenticate(email=request.data.get("email"),password=request.data.get("password"))

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh),'access': str(refresh.access_token)},status=status.HTTP_200_OK)

            return Response({"erro":"credencias invalidas"},status=status.HTTP_401_UNAUTHORIZED)

        return Response({"erro":"entre com o email e a senha"},status=status.HTTP_400_BAD_REQUEST)