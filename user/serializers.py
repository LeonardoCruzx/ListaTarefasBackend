from .models import *

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            "password",
            "is_superuser",
            "date_joined",
            "groups",
            "user_permissions",
            "last_login"
        ]

    

