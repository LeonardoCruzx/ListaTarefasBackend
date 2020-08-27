
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer

from rest_framework_simplejwt.tokens import RefreshToken

class UserList(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self,request,format=None):
        if(User.check_credentials(request)):
            try:
                user = User.objects.create_user(
                    email=request.data.get("email"),
                    password=request.data.get("password"),
                )
            except IntegrityError as e:
                return Response({"erro":"este email ja foi registrado"},status=status.HTTP_400_BAD_REQUEST)
            except ValidationError:
                return Response({"erro":"digite um email valido"}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError as e:
                return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),'access': str(refresh.access_token)},status=status.HTTP_201_CREATED)   

        return Response({"erro":"entre com o email e a senha"},status=status.HTTP_400_BAD_REQUEST)
