from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True
    )

    class Meta:
        ordering = ["-created_at"]