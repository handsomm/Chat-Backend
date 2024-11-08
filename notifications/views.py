# notifications/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .serializers import NotificationSerializer, FCMTokenSerializer
from .models import FCMToken
from .utils import send_fcm_notification

class SendNotificationAPIView(APIView):
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            registration_id = serializer.validated_data['registration_id']
            message_title = serializer.validated_data['message_title']
            message_body = serializer.validated_data['message_body']

            response = send_fcm_notification(registration_id, message_title, message_body)
            
            if response.status_code == 200:
                return Response({"message": "Notification sent successfully!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": response.json()}, status=response.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreFCMTokenAPIView(APIView):
    def post(self, request):
        serializer = FCMTokenSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['fcm_token']
            
            # Add a new token or update timestamp if it already exists
            fcm_token, created = FCMToken.objects.update_or_create(
                fcm_token=token,
                defaults={'updated_at': timezone.now()}
            )

            message = "FCM token stored successfully!" if created else "FCM token updated successfully!"
            return Response({"message": message}, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)