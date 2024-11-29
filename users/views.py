from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ValidationError
from .models import CustomUser

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'id': str(user.id),
                    'email': user.email,
                    'name': user.name,
                    'status': user.status,
                    'profile_image': user.profile_image,
                }
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def activate_user_view(request, id):
    try:
        print(id, "00000")
        
        # Fetch the user from the database
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            raise NotFound({'error': 'User not found.'})

        # Use the `activate` method from the custom manager
        activated_user = CustomUser.objects.activate(user)
        if activated_user:
            return Response({'message': 'User activated successfully.', 'status': activated_user.status})
        else:
            return Response({'message': 'User is already active.'}, status=400)

    except ValidationError as e:
        return Response({'error': str(e)}, status=400)