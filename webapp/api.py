from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Register
@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')

    error = {'error':'username and password are requide.'}
    if not username or not password:
        return Response(error, status= status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        error = {'error': 'username is already taken.'}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=username,
        password=password,
        email=email,
    )

    message = {'message':'user created successfully.'}
    return Response(message, status=status.HTTP_201_CREATED)


# login
@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    print("Username:", username)
    print("Password:", password)


    user = authenticate(username=username, password=password)
    print("Username:", username)
    print("Password:", password)
    print("User:", user)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        refresh_access_token = {
            'refresh' : str(refresh),
            'access' : str(access),
        }
        return Response(refresh_access_token)
    error = {'error':'invalid credentials'}
    return Response(error, status=status.HTTP_401_UNAUTHORIZED)

# Logout (blacklist refresh token)
@api_view(['POST'])
def api_logout(request):
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        message = { 'message' : 'Loged out successfully. '}
        return Response(message, status=status.HTTP_200_OK)
    except Exception:
        error = {'error' : 'invalid token'}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


