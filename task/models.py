from django.db import models

class Task(models.Model):
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="task"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    final_date = models.DateTimeField(
        null=True
    )
    content = models.TextField(
        null=False,
    )
    concluded = models.BooleanField(
        null=False,
        default=False
    )
    category = models.ForeignKey(
        "core.Category",
        on_delete=models.CASCADE,
        null=False
    )

    class Meta:
        ordering = ["-created_at"]