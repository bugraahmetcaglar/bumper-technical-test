from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from assignment.generics import StandardResultsSetPagination
from guestbook.models import GuestBook
from guestbook.serializers import GuestBookRetrieveUpdateDestroySerializer, GuestBookListCreateSerializer


class GuestBookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookRetrieveUpdateDestroySerializer
    lookup_field = 'id'


class GuestBookListCreateAPIView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    pagination_class = StandardResultsSetPagination
    serializer_class = GuestBookListCreateSerializer
    queryset = GuestBook.objects.all()
    filterset_fields = ['name']

    def list(self, request, *args, **kwargs):
        obj = GuestBook.objects.all()
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, 200)
