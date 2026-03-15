from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Records
from .serializers import RecordsSerializer


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

    user = User.objects.create_user(
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


# CRUD API
# ---get all endpoint
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def  api_get_records(request):
    records = Records.objects.all()
    serializer = RecordsSerializer(records, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# --get single endpoint
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_record(request, pk):
    try:
        record = Records.objects.get(id=pk)
    except Records.DoesNotExist:
        error = {'error' : 'Record not found.'}
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    serializer = RecordsSerializer(record)
    return Response(serializer.data)


# --create endpoint
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_record(request):
    serializer = RecordsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---edit record endpoint
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_record(request, pk):
    try:
        record = Records.objects.get(id=pk)
    except Records.DoesNotExist:
        error ={'error' : 'Record not found.'}
        return Response(error, status=status.HTTP_404_NOT_FOUND)
    serializer = RecordsSerializer(record, data=request.data)
    if  serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -- Delete endpoint
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_record(request, pk):
    try:
        record = Records.objects.get(id=pk)
    except Records.DoesNotExist:
        error ={'error' : 'Record not found.'}
        return Response(error, status=status.HTTP_404_NOT_FOUND)
    record.delete()
    message = {'message' : 'Record deleted successfully'}
    return Response(message, status=status.HTTP_200_OK)

