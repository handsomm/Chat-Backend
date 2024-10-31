# notifications/utils.py
import json
import requests
from django.conf import settings
from google.oauth2 import service_account
from google.auth.transport.requests import Request

def get_access_token():
    """Generate an access token using the service account."""
    credentials = service_account.Credentials.from_service_account_file(
        settings.FCM_SERVICE_ACCOUNT_KEY_PATH,
        scopes=["https://www.googleapis.com/auth/firebase.messaging"],
    )
    credentials.refresh(Request())
    return credentials.token

def send_fcm_notification(registration_token, title, body):
    """Send notification using FCM HTTP v1 API."""
    access_token = get_access_token()
    
    # Construct the notification payload
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    # Prepare FCM message payload
    fcm_message = {
        "message": {
            "token": registration_token,
            "notification": {
                "title": title,
                "body": body,
            }
        }
    }

    # Make a POST request to FCM API
    response = requests.post(
        f"https://fcm.googleapis.com/v1/projects/{settings.FCM_PROJECT_ID}/messages:send",
        headers=headers,
        data=json.dumps(fcm_message),
    )

    # Return the response
    return response
