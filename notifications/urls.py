# notifications/urls.py
from django.urls import path
from .views import SendNotificationAPIView

urlpatterns = [
    path('send-notification/', SendNotificationAPIView.as_view(), name='send-notification'),
]
