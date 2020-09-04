from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True
    )
    icon = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )

    class Meta:
        ordering = ["-name"]