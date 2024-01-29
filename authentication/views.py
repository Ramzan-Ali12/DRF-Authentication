from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer
# signup
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            response_data = {
                'Success': 'Signup Successfully',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# login
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email') 
        password = request.data.get('password')

        user = None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            pass

        if not user or not user.check_password(password):
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        # Authenticate the user using Django's authenticate method
        user = authenticate(request, username=user.username, password=password)

        if user:
            # token returns the tuple object in this tuple one is token and second is boolean to check wheather the token is created or not
            token = RefreshToken.for_user(user=user)
            response_data = {
                'success': 'Login Successfully',
                'access_token': str(token.access_token),
                'refresh_token': str(token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            }
            # Add the token to the response headers
            response = Response(response_data, status=status.HTTP_200_OK)
            response['Authorization'] = token
            return response

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
