# notifications/serializers.py
from rest_framework import serializers

class NotificationSerializer(serializers.Serializer):
    registration_id = serializers.CharField(max_length=255)
    message_title = serializers.CharField(max_length=255)
    message_body = serializers.CharField(max_length=1024)
