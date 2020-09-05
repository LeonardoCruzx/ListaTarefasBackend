from .manager import UserManager

from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    objects = UserManager()
    username = None

    email = models.EmailField(
        null=False,
        unique=True,
    )
    nick = models.CharField(
        max_length=30,
        null=True,
        unique=True
    )
    last_login = models.DateTimeField(
        verbose_name="last login",
        auto_now=True,
        null=True
    )

    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.nick
    
    @staticmethod
    def check_credentials(request):
        email = request.data.get("email")
        password = request.data.get("password")
        if(email and password is not None):
            return True
        return False
