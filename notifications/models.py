# notifications/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

class FCMToken(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='fcm_tokens', 
        null=True, 
        blank=True  # Allow tokens without a user
    )
    fcm_token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email if self.user else 'No User'} - {self.fcm_token}"
