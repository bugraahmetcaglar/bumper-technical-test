from datetime import datetime

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from assignment.constants import BaseResponse

import django_filters


class ExtendedCreateAPIView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = BaseResponse.success_response(status_code=201, message="Successfully created.")
        return JsonResponse(status.HTTP_201_CREATED, response)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @swagger_auto_schema(operation_summary="Create a data")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExtendedUpdateAPIView(UpdateAPIView):

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, updated_at=datetime.utcnow())


class ExtendedRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):
        # serializer.save(updated_by=self.request.user, updated_at=datetime.utcnow())
        pass


class ExtendedListCreateAPIView(ListCreateAPIView):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']
    ordering = ('-created_at',)

    def perform_create(self, serializer):
        # serializer.save(created_by=self.request.user)
        pass


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 1000
