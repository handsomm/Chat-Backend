from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['POST'])
def login_view(request):
  try:
    data = json.load(request.data)
    serializer = LoginSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)

    response_data = {
      'token': token.key,
      'user': {
          'id': str(user.id),
          'email': user.email,
          'name': user.name,
          'status': user.status,
          'profile_image': user.profile_image,
      }
    }

    return JsonResponse(response_data)
  
  except json.JSONDecodeError:
    return JsonResponse({'error': 'Invalid JSON.'}, status=400)