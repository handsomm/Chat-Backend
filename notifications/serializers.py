# notifications/serializers.py
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import FCMToken


class NotificationSerializer(serializers.Serializer):
    registration_id = serializers.CharField(max_length=255)
    message_title = serializers.CharField(max_length=255)
    message_body = serializers.CharField(max_length=1024)

class FCMTokenSerializer(serializers.ModelSerializer):
    fcm_token = serializers.CharField(max_length=255)

    class Meta:
        model = FCMToken
        fields = ['fcm_token']