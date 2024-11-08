# notifications/urls.py
from django.urls import path
from .views import SendNotificationAPIView, StoreFCMTokenAPIView

urlpatterns = [
    path('send-notification/', SendNotificationAPIView.as_view(), name='send-notification'),
    path('remove-fcm-key/', SendNotificationAPIView.as_view(), name='send-notification'),
    path('store-fcm-token/', StoreFCMTokenAPIView.as_view(), name='store_fcm_token'),
]
