from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer
import pdb
from drf_spectacular.utils import extend_schema


# signup
@extend_schema(request=UserSerializer)
@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # get the password
            raw_password = request.data.get("password")
            # Hash the password using make_password method
            hashed_password = make_password(raw_password)

            # Save the user with the hashed password
            user = serializer.save(password=hashed_password)
            return Response(
                {
                    "Success": "Signup Successfully",
                    "User": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# login
@extend_schema(request=UserSerializer)
@api_view(["POST"])
def login(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "User does not exist!"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Check the password using user.check_password
        if not user.check_password(password):
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Authenticate the user using Django's authenticate method
        user = authenticate(request, username=user.username, password=password)

        if user:
            # Obtain a refresh token
            refresh = RefreshToken.for_user(user)
            # Return the response
            return Response(
                {
                    "Success": "Login Successful!",
                    "User": {
                        "access_token": str(refresh.access_token),
                        "refresh_token": str(refresh),
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    },
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )
