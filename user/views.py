# Bugra Ahmet Caglar
import requests
from django.core.mail import send_mail
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework_jwt.settings import api_settings

from rest_framework.generics import ListAPIView

from rest_framework.response import Response

from assignment.constants import BaseResponse
from assignment.generics import StandardResultsSetPagination
from assignment.settings import EMAIL_FROM_EMAIL
from user.models import User
from user.serializers import UserLoginSerializer, UserRegisterSerializer, UserDetailSerializer, \
    UserForgetPasswordSerializer, UserLogoutSerializer, UserListSerializer, UserResetPasswordSerializer

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginAPIView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(operation_summary="User login API")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny, ]

    @swagger_auto_schema(operation_summary="Create a new user API")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = BaseResponse.success_response(message="User successfully created.", status_code=201)
        return Response(data=response, status=200)


class UserDetailAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class UserLogoutAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserLogoutSerializer

    @swagger_auto_schema(operation_summary="Logout api")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = BaseResponse.success_response(message="User successfully logged out.", status_code=201)
        return Response(data=response, status=200)


class UserListAPIView(ListAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = UserListSerializer
    pagination_class = StandardResultsSetPagination
    queryset = User.objects.all()
    lookup_field = 'id'
