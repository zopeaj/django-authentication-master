from django.shortcuts import render, redirect
from rest_framework.views.decorator import api_view
from rest_framework.response import Response
from rest_framework import status
from account.core.business.abstracts.AccountService import accountService
from account.core.business.concretes.AuthManager import authManager
# Create your views here.

@api_view(['POST'])
def register(request):
    data = request.data
    if data is None:
        user = accountService.save(data)
        return Response({"detail": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response({"error": "Error while trying to register user"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    password = request.data.get("password")
    username = request.data.get("username")
    user = authManager.setAuthentication(password, username)
    request.headers.update({'is_authenticated': True})
    if user is not None:
        response = Response(status=status.HTTP_200_OK)
        response['is_authenticated'] = True
        return response
    return Response({"error": "Incorrect Username or Password"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def logout(request):
    username = request.data.get("username")
    authManager.removeAuthentication(username)
    return Response({'detail': 'user successfully logged out'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def account_home(request):
    if request.headers.get('is_authenticated'):
        vd = Video.Objects.all()
        return Response({'vd': vd}, status=status.HTTP_200_OK)
    return Response({'error': 'User not authenticated'}, status=status.HTTP_403_AUTHENTICATED)



