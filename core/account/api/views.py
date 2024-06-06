from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView

from core.account.api.serializers import *

class AccountAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_fields = [f.name for f in User._meta.get_fields()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = User.objects.create_user(**serializer.validated_data)
        user.save()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class LoginAPIView(viewsets.GenericViewSet, CreateModelMixin):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        password = serializer.validated_data['password']

        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)

        return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)