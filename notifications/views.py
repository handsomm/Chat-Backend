# notifications/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer
from .utils import send_fcm_notification

class SendNotificationAPIView(APIView):
    def post(self, request):
        print(request, "--------")
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
